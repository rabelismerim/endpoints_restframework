"""Captura a API real com dados fictícios em um banco temporário isolado.
Uso: python docs/capture_screenshots.py [--browser CAMINHO]
Requer Chrome/Chromium/Edge instalado. Não acessa o db.sqlite3 do projeto.
"""
import argparse
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "screenshots"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser", help="Caminho do executável Chrome, Chromium ou Edge")
    args = parser.parse_args()
    candidates = [args.browser, shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("msedge"),
                  r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                  r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]
    browser = next((str(p) for p in candidates if p and Path(p).is_file()), None)
    if not browser:
        parser.error("Navegador não encontrado. Informe --browser CAMINHO.")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    flags = {"creationflags": subprocess.CREATE_NO_WINDOW} if os.name == "nt" else {}
    with tempfile.TemporaryDirectory(prefix="mentoria-captures-") as temp:
        env = {**os.environ, "DJANGO_DB_NAME": str(Path(temp) / "demo.sqlite3"),
               "DJANGO_DEBUG": "true", "DJANGO_ALLOWED_HOSTS": "127.0.0.1,localhost"}
        for command in (["migrate", "--noinput"], ["seed_demo"]):
            subprocess.run([sys.executable, "manage.py", *command], cwd=ROOT, env=env, check=True, **flags)
        with socket.socket() as sock:
            sock.bind(("127.0.0.1", 0))
            port = sock.getsockname()[1]
        with open(Path(temp) / "server.log", "w", encoding="utf-8") as log:
            server = subprocess.Popen([sys.executable, "manage.py", "runserver", f"127.0.0.1:{port}", "--noreload"],
                                      cwd=ROOT, env=env, stdout=log, stderr=log, **flags)
            try:
                base = f"http://127.0.0.1:{port}/api/polls/"
                for _ in range(100):
                    try:
                        with urllib.request.urlopen(base, timeout=1) as response:
                            if response.status == 200:
                                break
                    except OSError:
                        time.sleep(0.1)
                else:
                    raise RuntimeError("A API não iniciou para captura.")
                for filename, path in (("api-root.png", ""), ("alunos.png", "aluno/"), ("tarefas.png", "reuniao_tarefa/")):
                    result = subprocess.run([
                        browser, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
                        f"--user-data-dir={Path(temp) / 'browser'}", "--window-size=1440,1100",
                        "--hide-scrollbars", "--virtual-time-budget=2000",
                        f"--screenshot={OUTPUT / filename}", base + path,
                    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=40, **flags)
                    if result.returncode or not (OUTPUT / filename).exists():
                        raise RuntimeError(result.stderr.decode(errors="replace"))
                    print(f"Captura: {OUTPUT / filename}")
            finally:
                server.terminate()
                server.wait(timeout=10)


if __name__ == "__main__":
    main()

from django.shortcuts import render
from .models import reuniao
from .models import reuniao_tarefa
from .models import coach
from .models import coachee
from .models import coach_coachee
from .models import competencia

def list(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(coach).list(request, *args, **kwargs)

def list(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(coachee).list(request, *args, **kwargs)

def list(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(coach_coachee).list(request, *args, **kwargs)

def list(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(reuniao).list(request, *args, **kwargs)

def list(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(reuniao_tarefa).list(request, *args, **kwargs)

def list(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(competencia).list(request, *args, **kwargs)
    
def retrieve(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(coach).retrieve(request, *args, **kwargs)

def retrieve(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(coachee).retrieve(request, *args, **kwargs)

def retrieve(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(coach_coachee).retrieve(request, *args, **kwargs)

def retrieve(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(reuniao).retrieve(request, *args, **kwargs)

def retrieve(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(reuniao_tarefa).retrieve(request, *args, **kwargs)

def retrieve(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(competencia).retrieve(request, *args, **kwargs)
    
def update(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(coach).update(request, *args, **kwargs)

def update(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(coachee).update(request, *args, **kwargs)

def update(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(coach_coachee).update(request, *args, **kwargs)

def update(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(reuniao).update(request, *args, **kwargs)

def update(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(reuniao_tarefa).update(request, *args, **kwargs)

def update(self, request, *args, **kwargs):
        self._set_user_attributes(request)
        return super(competencia).update(request, *args, **kwargs)
    
def options(self, request, *args, **kwargs):
        #self.is_creating = request._request.META['HTTP_REFERER'].split('/')[-1] == 'new'
        self._set_user_attributes(request)
        return super(coach).options(request, *args, **kwargs)

def options(self, request, *args, **kwargs):
        #self.is_creating = request._request.META['HTTP_REFERER'].split('/')[-1] == 'new'
        self._set_user_attributes(request)
        return super(coachee).options(request, *args, **kwargs)

def options(self, request, *args, **kwargs):
        #self.is_creating = request._request.META['HTTP_REFERER'].split('/')[-1] == 'new'
        self._set_user_attributes(request)
        return super(coach_coachee).options(request, *args, **kwargs)

def options(self, request, *args, **kwargs):
        #self.is_creating = request._request.META['HTTP_REFERER'].split('/')[-1] == 'new'
        self._set_user_attributes(request)
        return super(reuniao).options(request, *args, **kwargs)

def options(self, request, *args, **kwargs):
        #self.is_creating = request._request.META['HTTP_REFERER'].split('/')[-1] == 'new'
        self._set_user_attributes(request)
        return super(reuniao_tarefa).options(request, *args, **kwargs)

def options(self, request, *args, **kwargs):
        #self.is_creating = request._request.META['HTTP_REFERER'].split('/')[-1] == 'new'
        self._set_user_attributes(request)
        return super(competencia).options(request, *args, **kwargs)
    

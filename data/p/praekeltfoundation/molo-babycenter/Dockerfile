FROM praekeltfoundation/molo-bootstrap:4.4.11-onbuild  
  
ENV DJANGO_SETTINGS_MODULE=babycenter.settings.docker \  
CELERY_APP=babycenter \  
CELERY_WORKER=1 \  
CELERY_BEAT=1  
  
RUN LANGUAGE_CODE=en django-admin compilemessages && \  
django-admin collectstatic --noinput && \  
django-admin compress  
  
CMD ["babycenter.wsgi:application", "--timeout", "1800"]  


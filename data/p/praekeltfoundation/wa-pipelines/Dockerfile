FROM praekeltfoundation/django-bootstrap  
  
COPY . /app  
RUN pip install -e .  
  
ENV DJANGO_SETTINGS_MODULE app.settings  
ENV CELERY_APP app  
ENV CELERY_WORKER 1  
RUN django-admin collectstatic --noinput  
  
CMD ["app.wsgi:application"]  


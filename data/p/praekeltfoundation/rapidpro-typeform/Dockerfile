FROM praekeltfoundation/django-bootstrap:py2  
  
COPY . /app  
RUN pip install -e .  
  
ENV DJANGO_SETTINGS_MODULE=rapidform.settings  
  
CMD ["rapidform.wsgi:application"]  


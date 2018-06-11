FROM zhongpei/django-base  
MAINTAINER Peter McConnell <peter.mcconnell@rehabstudio.com>  
  
# start supervisor to run our wsgi server  
CMD cd /opt/app/ && /opt/venv/bin/python manage.py runserver 0.0.0.0:5000  
  
EXPOSE 5000  


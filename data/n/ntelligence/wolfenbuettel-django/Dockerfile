FROM django:1.8-python2  
  
MAINTAINER Andreas Helmberger <public@ahelmberger.de>  
  
ENV VIRTUAL_HOST wb-django.ahelmberger.de  
  
COPY . /usr/src/app  
  
WORKDIR /usr/src/app  
  
CMD python manage.py runserver 0.0.0.0:8000  


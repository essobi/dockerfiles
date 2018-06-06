FROM django:onbuild  
VOLUME /usr/src/app/app/media  
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000  


From python:3.6.4-alpine3.7  
COPY requirements.txt /src/  
WORKDIR /src  
RUN pip install -r requirements.txt  
VOLUME app  
  
EXPOSE 8000  
WORKDIR /src/app  
CMD /usr/local/bin/python manage.py runserver 0.0.0.0:8000  


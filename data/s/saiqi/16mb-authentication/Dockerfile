FROM python:3  
MAINTAINER Julien Bernard <julien.bernard.iphone@gmail.com>  
  
RUN pip3 install pytest flask-restful flask-mongoengine gunicorn passlib pyjwt  
  
RUN mkdir /service  
  
COPY application /service/application  
  
EXPOSE 5000  
  
WORKDIR /service  
  
CMD ["gunicorn","-b",":5000","application.app:app"]


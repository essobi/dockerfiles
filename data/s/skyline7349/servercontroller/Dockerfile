FROM python:latest  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y libxmlrpc-c++8-dev  
EXPOSE 8000  
COPY . /app  
WORKDIR /app  
RUN pip install -r requirements.txt  
CMD python manage.py runserver 0.0.0.0:8000


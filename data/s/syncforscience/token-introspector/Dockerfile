FROM python:3  
MAINTAINER Josh Mandel  
  
# Install required packages  
RUN apt-get update  
RUN apt-get install -y \  
supervisor  
RUN apt-get clean  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app  
  
# Set the environment  
ENV FLASK_APP /usr/src/app/app.py  
ENV API_SERVER http://api:8080/baseDstu2  
ENV API_SERVER_NAME 'Mainline Clinic'  
CMD ["supervisord", "-c", "supervisord.conf"]  


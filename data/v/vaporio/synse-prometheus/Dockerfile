FROM python:3.6-alpine  
MAINTAINER Klemente Gilbert-Espada <klemente@vapor.io>  
  
ADD ./requirements.txt requirements.txt  
  
# Install dependencies  
RUN pip3 install -r requirements.txt  
  
ADD . /code  
WORKDIR /code  
  
# Expose our API endpoint port.  
EXPOSE 9243  
# Define default command  
CMD ["python", "runserver.py"]  


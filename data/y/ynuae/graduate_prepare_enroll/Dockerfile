# Set the base image to nginx  
FROM python:2  
# File Author / Maintainer  
MAINTAINER Liudonghua <liudonghua123@gmail.com>  
  
# update the repository sources list  
RUN apt-get update  
  
# install vim for quick modify  
RUN apt-get install -y vim  
  
RUN mkdir -p /app  
  
COPY requirements.txt /app  
  
WORKDIR /app  
  
# install dependencies  
RUN pip install -v -r requirements.txt  
  
COPY . /app  
  
CMD ["python", "app.py"]  


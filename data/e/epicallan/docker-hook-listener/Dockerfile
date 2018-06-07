# start with a base image  
FROM ubuntu:trusty  
MAINTAINER epicallan <epicallan.al@gmail.com>  
  
# install dependencies  
RUN apt-get update  
RUN apt-get install -y python-pip  
RUN pip install flask  
  
# update working directories  
ADD ./app /app  
  
CMD python app/app.py  


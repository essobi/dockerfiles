# start with a base image  
FROM ubuntu:14.10  
# install dependencies  
RUN apt-get -y update  
RUN apt-get install -y python python-dev python-pip libffi-dev libssl-dev
libmagickwand-dev  
  
# add requirements.txt and install  
ADD . /code  
RUN pip install -r /code/requirements.txt  
  
EXPOSE 5000  
# set working diretory  
WORKDIR /code  
  
CMD honcho start  


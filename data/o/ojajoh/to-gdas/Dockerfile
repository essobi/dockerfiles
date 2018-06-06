FROM python:3.5  
MAINTAINER Joost Venema <joost.venema@kadaster.nl>  
  
# to-gdas  
#  
# VERSION 1.0  
# Needed to get output in detached mode  
ENV PYTHONUNBUFFERED 0  
# Clone latest to-gdas version from Github  
RUN git clone https://github.com/joostvenema/to-gdas.git  
  
# set workingdir  
WORKDIR /to-gdas  
  
# Install packages  
RUN pip install -r requirements.txt  
  
# expose the default port  
EXPOSE 9090  
# bring app to live  
CMD [ "python", "./webapp.py" ]  


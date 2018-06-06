FROM debian:jessie  
MAINTAINER Niall Byrne <reading.crows@gmail.com>  
  
# Patch BASH  
RUN ln -sf /bin/bash /bin/sh  
  
# Create the RUN AS user  
RUN useradd -ms /bin/bash celery  
USER celery  
WORKDIR /home/celery  
  
# Configure the Home Directory  
ADD worker.py /home/celery/worker.py  
ADD bin /home/celery/bin/  
  
# Configure Packages and Remove all Unnecessary Dependencies  
USER root  
RUN bin/build.sh  
  
# Print list of packages still installed  
RUN dpkg --get-selections | grep -v deinstall  
  
# Start the application  
CMD "bin/launch.sh"  


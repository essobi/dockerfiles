FROM debian:jessie  
MAINTAINER Niall Byrne <reading.crows@gmail.com>  
  
# Patch BASH  
RUN ln -sf /bin/bash /bin/sh  
  
# Lock Down  
RUN useradd -ms /bin/bash webservice  
USER webservice  
WORKDIR /home/webservice  
  
# Install Pip Requirements  
ADD requirements /home/webservice/requirements  
ADD app /home/webservice/app  
ADD config.py /home/webservice/config.py  
ADD run.py /home/webservice/run.py  
ADD bin/launch.sh /home/webservice/bin/launch.sh  
ADD bin/build.sh /home/webservice/bin/build.sh  
ADD bin/cleanup /home/webservice/bin/cleanup  
RUN mkdir /home/webservice/database  
  
# Configure Packages and Remove all Unnecessary Dependencies  
# This is designed to reduce the size of the end docker image  
USER root  
RUN bin/build.sh  
  
# Configure Container  
EXPOSE 5000  
  
# Look for stuff to remove  
RUN dpkg --get-selections | grep -v deinstall  
  
# Execute a BASH shell  
USER webservice  
CMD bin/launch.sh  


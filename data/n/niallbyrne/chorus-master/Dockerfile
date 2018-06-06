FROM debian:jessie  
MAINTAINER Niall Byrne <reading.crows@gmail.com>  
  
# Patch BASH  
RUN ln -sf /bin/bash /bin/sh  
  
# Create the RUN AS user  
RUN useradd -ms /bin/bash webservice  
USER webservice  
WORKDIR /home/webservice  
  
# Configure the Home Directory  
ADD requirements /home/webservice/requirements  
ADD app /home/webservice/app  
ADD config.py /home/webservice/config.py  
ADD run.py /home/webservice/run.py  
ADD bin /home/webservice/bin  
ADD worker.py /home/webservice/worker.py  
  
# Configure Packages and Remove all Unnecessary Dependencies  
USER root  
RUN bin/build.sh  
  
# Configure Container Ports  
EXPOSE 5000  
# Print list of packages still installed  
RUN dpkg --get-selections | grep -v deinstall  
  
# Start the application  
CMD bin/launch.sh  


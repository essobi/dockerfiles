# fitbit galileo  
# a docker image to sunc fitbit devices  
# VERSION 1.0  
FROM google/python:latest  
MAINTAINER ARrrr "ar@lightonthehill.net"  
# install all packages needed by galileo (may be redundant but done in case
the base image is  
# changed)  
RUN apt-get update  
RUN apt-get install -y \  
usbutils \  
python-pip \  
python-usb \  
python-requests  
  
RUN pip install galileo  
  
#start to daemon to run fitbit sync every 15 minutes (this can be overwritten
using 'docker run')  
CMD ["galileo", "daemon"]  


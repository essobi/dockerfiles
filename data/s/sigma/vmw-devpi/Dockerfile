FROM python:2.7.9-onbuild  
MAINTAINER Yann Hodiquey <hodiquey@vmware.com>  
  
EXPOSE 3141  
VOLUME ["/var/lib/devpi"]  
  
CMD ["devpi-server", "--host=0.0.0.0", "--port=3141", "--
serverdir=/var/lib/devpi"]  


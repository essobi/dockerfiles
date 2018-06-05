FROM ubuntu:14.04  
MAINTAINER Lukas Hetzenecker <lukas.hetzenecker@gmail.com>  
  
RUN apt-get update  
  
# Install python packages  
RUN apt-get install -y --force-yes python-dev python-pip  
RUN apt-get install -y --force-yes libssl-dev libffi-dev  
RUN pip install python-etcd  
RUN pip install boto  
  
# Add update script  
ADD ./update.py /scripts/update.py  
  
# Run the boot script  
CMD ["/usr/bin/python", "/scripts/update.py"]  
  


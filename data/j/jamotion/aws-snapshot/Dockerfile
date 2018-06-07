FROM phusion/baseimage  
MAINTAINER Renzo Meister <rm@jamotion.ch>  
  
# Install python setup tools  
RUN apt-get update &&\  
apt-get install -y python-setuptools &&\  
easy_install pip  
  
# Add python package and sample config  
ADD snapshot/* /opt/aws/snapshot/  
  
# Install dependencies  
RUN cd /opt/aws/snapshot/; pip install -r requirements.txt  
  
# Share the config and log volumes  
VOLUME ["/etc/aws/snapshot", "/var/log/aws"]  
  
# Run the command on container startup  
CMD ["python", "/opt/aws/snapshot/init.py"]  
  


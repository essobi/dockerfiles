# barbican  
#  
# VERSION 0.1  
#zenphu :: Zenaptix-Phusion  
# Pull base image.  
FROM phusion/baseimage:0.9.19  
MAINTAINER Calvin Maree , cloudcalvin@me.com  
  
  
# Add Repos and Install Packages  
#ADD yum.repos.d/ /etc/yum.repos.d  
#RUN yum update  
RUN apt-get update && apt-get install -y python-pip gcc libffi-dev python-dev
libssl-dev libsqlite3-dev  
  
# Add Configs and Scripts  
ADD scripts/ /opt/docker-scripts  
ADD barbican/ /opt/barbican-src  
  
RUN /opt/docker-scripts/install_barbican.sh  
  
EXPOSE 9311  
CMD /opt/docker-scripts/start_barbican.sh  


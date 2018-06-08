FROM peerlibrary/runit  
  
MAINTAINER Mitar <mitar.docker@tnode.com>  
  
EXPOSE 27017/tcp  
  
COPY ./etc/apt /etc/apt  
  
RUN apt-get update -q -q && \  
apt-get install -t wheezy-backports mongodb --yes --force-yes  
  
COPY ./etc /etc  


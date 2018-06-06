FROM stackbrew/ubuntu:14.04  
MAINTAINER Spencer Herzberg "http://github.com/sherzberg/docker-curdserver"  
RUN apt-get update -qq  
  
RUN apt-get install -y python-dev python-pip libevent-dev  
RUN pip install flask==0.10.1 gevent==0.13.8  
RUN pip install curdling==0.4.0  
  
RUN mkdir -p /var/wheelhouse  
  
EXPOSE 8000  
VOLUME ["/var/wheelhouse"]  
  
CMD ["curd-server", "/var/wheelhouse"]  


# Dockerfile for adding supervisor to a base image  
FROM shift/coreos-ubuntu-etcd:latest  
  
MAINTAINER Vincent Palmer <shift-gh@someone.section.me>  
  
ENV HOME /root  
RUN apt-get update && apt-get install -y python-pip  
RUN pip install supervisor-logging  
RUN mkdir -p /var/log/supervisor && mkdir -p /etc/supervisor/conf.d  
  
ADD files/supervisor.conf /etc/supervisor.conf  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  


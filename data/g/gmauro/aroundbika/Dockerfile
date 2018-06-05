# Based on gmauro/debian-ansible  
FROM gmauro/debian-ansible  
MAINTAINER Gianmauro Cuccuru <gmauro@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN git clone https://github.com/gmauro/aroundBika /tmp/aroundBika  
WORKDIR /tmp/aroundBika  
RUN ansible-playbook aroundBika.yml  
  
EXPOSE 8081  
RUN apt-get update && apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]


# jmvrbanac/simple-barbican  
#  
# Docker image for running Barbican for development and testing ONLY  
#  
FROM ubuntu:latest  
MAINTAINER John Vrbanac <john.vrbanac@linux.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update; apt-get install -y vim git python-pip python-dev python-
psycopg2 libsqlite3-dev libffi-dev libssl-dev  
  
RUN mkdir -p /opt/docker_app/  
RUN git clone https://github.com/cloudkeep/barbican.git
/opt/docker_app/barbican  
RUN pip install uwsgi  
RUN pip install /opt/docker_app/barbican  
  
COPY etc/barbican /etc/barbican  
COPY start.sh /opt/docker_app/  
  
# Make sure we have a place to put all the things  
RUN mkdir -p /var/lib/barbican; mkdir -p /var/log/barbican  
RUN touch /var/log/barbican/barbican-api.log  
  
VOLUME /etc/barbican  
EXPOSE 9311 9312  
CMD ["bash", "/opt/docker_app/start.sh"]  


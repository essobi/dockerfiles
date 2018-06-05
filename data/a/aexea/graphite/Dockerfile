FROM ubuntu:16.04  
MAINTAINER Aexea Carpentry  
  
RUN apt-get update && \  
apt-get install --yes graphite-carbon graphite-api gunicorn3  
  
EXPOSE 2003 8000  
VOLUME "/var/lib/graphite"  
CMD ["/usr/bin/carbon-cache", "--config=/etc/carbon/carbon.conf", "--
pidfile=/var/run/carbon-cache.pid", "--logdir=/var/log/carbon/", "--nodaemon",
"start" ]  


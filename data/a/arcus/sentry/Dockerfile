FROM debian:jessie  
MAINTAINER Arcus "http://arcus.io"  
RUN apt-get update  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y python python-dev libpq-dev python-setuptools python-
memcache  
RUN easy_install pip  
RUN pip install sentry[postgres]  
ADD sentry.conf.py /etc/sentry.conf.py  
ADD run.sh /usr/local/bin/run  
EXPOSE 9000 9001/udp  
CMD ["/usr/local/bin/run"]  


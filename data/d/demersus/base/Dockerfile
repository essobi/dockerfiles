FROM ubuntu:latest  
MAINTAINER Nik Petersen (demersus@gmail.com)  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y ca-certificates curl inotify-tools pwgen supervisor
unzip wget  
RUN RUN apt-get install -y python-pip && pip install supervisor-stdout  
RUN apt-get clean  
ADD supervisor.conf /etc/supervisor/conf.d/00-init.conf  
ADD init /init  
RUN chmod +x /init/supervisor  
CMD /init/supervisor  


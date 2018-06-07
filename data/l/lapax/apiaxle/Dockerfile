# apiaxle  
# this file is at https://github.com/lexlapax/dockerfile-
apiaxle/blob/master/Dockerfile  
# based on install instructions from  
# http://apiaxle.com/docs/try-it-now/  
FROM ubuntu:precise  
MAINTAINER Lex Lapax <lexlapax@gmail.com>  
  
# Update the APT cache  
ENV DEBIAN_FRONTEND noninteractive  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN apt-get update ; apt-get upgrade --fix-missing -y  
  
# install essentials  
RUN apt-get install python-software-properties -y  
  
# Hack for initctl  
# See: https://github.com/dotcloud/docker/issues/1024  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Install and setup project dependencies  
# start with specifics for this image  
RUN add-apt-repository ppa:chris-lea/redis-server -y  
RUN add-apt-repository ppa:chris-lea/node.js -y  
RUN apt-get update  
RUN apt-get install -y supervisor libxml2 redis-server rlwrap nodejs  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN mkdir -p /var/log/supervisord  
  
RUN locale-gen en_US en_US.UTF-8  
  
RUN echo "ulimit -n 4096" >> /etc/default/redis  
  
# Done base image setup  
# install dev essentials and remove them after compile to reduce image size  
RUN \  
apt-get install build-essential libtool libxml2-dev libssl-dev -y ; \  
npm install -g apiaxle-repl apiaxle-proxy apiaxle-api ; \  
apt-get remove build-essential libxml2-dev libssl-dev libtool -y ; \  
apt-get autoremove -y  
  
# Expose Protocol Buffers and HTTP interfaces  
EXPOSE 3000  
#CMD ["apiaxle-proxy", "-f", "1", "-p", "3000", "-q"]  
CMD ["/usr/bin/supervisord", "-n"]  


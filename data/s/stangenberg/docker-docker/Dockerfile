FROM thstangenberg/baseimage:latest  
  
MAINTAINER Thorben Stangenberg <thorben@stangenberg.net>  
  
ENV DOCKER_LOG_LEVEL=info \  
DOCKER_PORT=2375  
# install prerequisites  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables  
  
# install docker  
RUN curl -sSL https://get.docker.com/ | sh  
  
# volume for docker  
VOLUME /var/lib/docker  
# expose default docker port  
EXPOSE 2375  
# add docker to runit  
ADD docker.sh /etc/service/docker/run  
RUN chmod 700 /etc/service/docker/run  
  
# Clean up when done.  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  


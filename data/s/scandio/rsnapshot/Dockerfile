FROM ubuntu:latest  
MAINTAINER Helmut Patay <helmut.patay@scandio.de>  
  
ENV COMPOSE_VERSION 1.4.2  
RUN apt-get update && apt-get install -y \  
curl \  
rsnapshot \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
ADD https://get.docker.io/builds/Linux/x86_64/docker-latest
/usr/local/bin/docker  
  
RUN curl -L
https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker && chmod +x /usr/local/bin/docker-compose  
  
COPY ./rsnapshot.conf /etc/rsnapshot.conf.default  
COPY ./start.sh /root/  
RUN chmod +x /root/start.sh  
  
VOLUME /source  
VOLUME /target  
VOLUME /config  
  
CMD /root/start.sh  


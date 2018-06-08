FROM ubuntu:16.04  
  
MAINTAINER Aaronstar, <jfeldt19@gmail.com>  
  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install curl ca-certificates openssl git tar bash sqlite
ejabberd erlang-dev make \  
&& adduser -h /home/container container \  
&& dpkg-reconfigure ejabberd  
  
USER  container  
ENV HOME /home/container  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  


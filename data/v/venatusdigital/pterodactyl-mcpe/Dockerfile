FROM ubuntu:16.04  
  
MAINTAINER Venatus Digital <hello@venatus.digital>  
  
RUN apt update \  
&& apt upgrade -y \  
&& apt install -y openssl bash automake perl gcc g++ make automake libtool
autoconf m4 curl \  
&& useradd -D -h /home/container container  
  
USER container  
ENV USER=container HOME=/home/container  
  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  


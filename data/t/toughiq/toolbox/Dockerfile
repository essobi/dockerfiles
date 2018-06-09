FROM debian:latest  
  
MAINTAINER toughiq <toughIQ@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends ngrep openssl curl wget mysql-
client sysbench host net-tools python \  
postgresql-client netcat traceroute telnet vim apache2-utils siege stress
stress-ng \  
&& apt-get clean all && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /bin  
CMD ["ping","localhost"]  
  


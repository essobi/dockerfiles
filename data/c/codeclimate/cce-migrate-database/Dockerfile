FROM ubuntu:14.04  
MAINTAINER Code Climate <hello@codeclimate.com>  
  
RUN apt-get update \  
&& apt-get install -y wget  
  
COPY migrate-database /  
  
RUN wget -O /bin/docker
https://get.docker.com/builds/Linux/x86_64/docker-1.6.0  
RUN chmod +x /bin/docker  
  
CMD ["./migrate-database"]  


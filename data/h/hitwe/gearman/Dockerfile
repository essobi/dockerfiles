FROM debian:jessie  
MAINTAINER Marko OS  
RUN \  
apt-get update \  
&& apt-get -y install gearman-job-server \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4730  
  
ENTRYPOINT [ "gearmand" ]  


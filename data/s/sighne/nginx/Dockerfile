FROM nginx:1.11  
MAINTAINER Sighne<sighne@foamyhorn.com>  
  
# Enable the Jessie backports repo  
RUN awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }'
/etc/apt/sources.list > /etc/apt/sources.list.d/backports.list  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install backport  
RUN apt-get -y install certbot -t jessie-backports  
  
# Add templates  
RUN mkdir -p /etc/docker-gen/templates  
ADD ./templates /etc/docker-gen/templates  


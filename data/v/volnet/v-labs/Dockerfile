FROM ubuntu:14.04  
MAINTAINER volnet "volnet@tom.com"  
RUN apt-get update && apt-get install -y nginx  
RUN echo 'Welcome to http://volnet.github.io/' >
/usr/share/nginx/html/index.html  
# ENTRYPOINT ["/usr/sbin/nginx"]  
WORKDIR ["/usr/share/nginx/html"]  
# CMD ["-g", "daemon off;"]  
VOLUME ["/home/parallels/Downloads"]  
LABEL author="volnet" email="volnet@tom.com"
homepage="http://volnet.github.io" version="1.0"  
ARG build  
ARG webapp_user=user  
ADD mylocalfile.tar.gz /opt/upload/ADD/  
COPY mylocalfile.tar.gz /opt/upload/COPY/  
EXPOSE 80  


FROM ubuntu:latest  
  
MAINTAINER LYC <imyikong@gmail.com>  
  
ADD aria2.conf /etc/aria2.conf  
ADD aria2.site.conf /etc/nginx/sites-enabled/default  
ADD entry.sh /entry.sh  
  
RUN apt-get update && \  
mkdir -p /site/download && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install aria2 && \  
apt-get install -y nginx && \  
chmod +x /entry.sh  
  
WORKDIR /site/  
VOLUME ["/site/download"]  
  
EXPOSE 80  
EXPOSE 6880  
ENV RPC_USER admin  
ENV RPC_PASSWD admin  
ENV FILE_EXPIRES 1440  
ENTRYPOINT ["/entry.sh"]  
  


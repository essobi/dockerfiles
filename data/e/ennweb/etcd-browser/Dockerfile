FROM ubuntu:14.04.3  
MAINTAINER Emre <e@emre.pm>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update && \  
apt-get install -y wget git && \  
wget -qO- https://deb.nodesource.com/setup | bash - && \  
apt-get install -y nodejs && \  
git clone https://github.com/henszey/etcd-browser.git /app  
  
EXPOSE 8000  
WORKDIR /app  
  
ENTRYPOINT ["node", "server"]  


FROM ubuntu:latest  
MAINTAINER Fernando Neto <fernando.neto@junglecloud.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y -q && \  
apt-get install -y mysql-client-5.6 nodejs-legacy npm curl wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g n azure-cli  
  
ADD restore.sh /restore.sh  
RUN chmod 0755 /restore.sh  
  
EXPOSE 3306  
ENTRYPOINT ["/restore.sh"]  


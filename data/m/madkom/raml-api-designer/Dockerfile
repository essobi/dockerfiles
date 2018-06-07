FROM debian:jessie  
  
MAINTAINER Dariusz Gafka <d.gafka@madkom.pl>  
  
RUN apt-get update -qq && \  
apt-get install -y nodejs npm --no-install-recommends && \  
npm install -g api-designer && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
rm -rf /var/lib/apt/lists/*  
  
CMD "api-designer"


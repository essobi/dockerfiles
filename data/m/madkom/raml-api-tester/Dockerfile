FROM debian:jessie  
  
MAINTAINER Dariusz Gafka <d.gafka@madkom.pl>  
  
RUN apt-get update -qq && \  
apt-get install -y nodejs npm nodejs-legacy --no-install-recommends && \  
npm install -g abao && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /contract  
  
CMD ["/bin/sh", "-c", "/usr/local/bin/abao /contract/api.raml $API_ENDPOINT"]


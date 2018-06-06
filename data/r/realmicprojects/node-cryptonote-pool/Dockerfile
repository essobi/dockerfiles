FROM debian:jessie-slim  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs-legacy npm git
libboost1.55-all \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD . /pool/  
WORKDIR /pool/  
  
RUN npm update  
  
EXPOSE 8117  
EXPOSE 3333  
EXPOSE 5555  
EXPOSE 7777  
CMD node init.js -config=/config/config.json  


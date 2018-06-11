FROM weyforth/nodejs-base:1.0  
MAINTAINER "Mike Farrow" <contact@mikefarrow.co.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /tmp  
  
RUN apt-get update -y && \  
apt-get install -y curl git && \  
curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get install -y nodejs && \  
apt-get remove --purge curl -y && \  
apt-get clean  
  
RUN npm install -g --no-optional nodemon@1.4.0  
  
COPY node_run /usr/local/bin/  
RUN chmod +x /usr/local/bin/node_run  
  
WORKDIR /data/src  
  
CMD ["node_run"]  


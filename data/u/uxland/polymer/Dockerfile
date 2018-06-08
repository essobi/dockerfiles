FROM node:latest  
MAINTAINER uxland <dev@uxland.es>  
  
RUN npm install -g bower && npm install -g polymer-cli --unsafe-perm && echo
'{"allow-root": true}' > /root/.bowerrc  
RUN apt-get update && apt-get upgrade -y && apt-get install apt-transport-
https  
RUN wget -q -O -
https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key
add -  
RUN echo "deb http://packages.cloudfoundry.org/debian stable main" | tee
/etc/apt/sources.list.d/cloudfoundry-cli.list  
RUN apt-get update && apt-get install cf-cli  


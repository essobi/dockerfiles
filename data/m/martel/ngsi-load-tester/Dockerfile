FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gettext-base \  
nano \  
&& rm -rf /var/lib/apt/lists/*  
  
# Bundle app source  
COPY run.sh /usr/src/app  
COPY contextBroker.yml.template /usr/src/app  
  
ENV ART_TARGET http://localhost:1026  
ENV ART_ARRIVALRATE 5  
ENV ART_DURATION 10  
ENV ART_RAMPTO 20  
ENV ART_DEBUG http,http:response  
  
CMD ["/bin/bash", "run.sh"]  


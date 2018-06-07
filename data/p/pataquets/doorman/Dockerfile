FROM node  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install git \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/ \  
&& \  
git clone \--single-branch --branch master
https://github.com/movableink/doorman.git && \  
cd /doorman && \  
npm install && \  
mv -vi conf.environment.js conf.js  
  
WORKDIR /doorman  
  
ENTRYPOINT [ "npm", "start" ]  


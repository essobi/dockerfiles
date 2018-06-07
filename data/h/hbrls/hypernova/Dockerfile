FROM node:8.6.0-slim  
  
  
COPY components/ /var/app/components  
COPY package.json /var/app/package.json  
COPY server.js /var/app/server.js  
  
# npm install  
RUN buildDeps='git make g++' && \  
apt-get update && apt-get install -y $buildDeps && \  
cd /var/app && npm install --no-optional --production && \  
npm cache clean --force && \  
apt-get purge -y --auto-remove $buildDeps && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3030  
CMD ["/usr/local/bin/node", "/var/app/server.js"]  


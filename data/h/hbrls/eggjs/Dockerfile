FROM node:8.9.1-slim  
  
EXPOSE 7001  
RUN mkdir -p /var/app && mkdir -p /var/app0  
WORKDIR /var/app  
  
# npm install  
RUN buildDeps='git make g++' && \  
apt-get update && apt-get install -y $buildDeps && \  
cd /var/app0 && npm install \  
egg@2.2.1 egg-view-nunjucks@2.1.3 egg-sequelize@3.1.0 pg@7.3.0 pg-hstore@2.3.2
vanilla.js@0.1.4 && \  
npm cache clean --force && \  
apt-get purge -y --auto-remove $buildDeps && \  
rm -rf /var/lib/apt/lists/*  
  
ENV NODE_ENV production  
  
  
CMD ["/usr/local/bin/node", "/var/app/index.js"]  
  


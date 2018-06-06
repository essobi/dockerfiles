FROM nodesource/wheezy:0.12.0  
MAINTAINER Brandon Papworth <brandon@powertower.com>  
  
COPY data/index.js data/thalassa-crowsnest-init.js data/package.json
/data/thalassa-crowsnest/  
  
RUN cd /data/thalassa-crowsnest && \  
npm install  
  
WORKDIR /data/thalassa-crowsnest  
VOLUME ["/data/thalassa-crowsnest"]  
EXPOSE 8080  
CMD ["node","index.js"]  


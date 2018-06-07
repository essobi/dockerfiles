FROM mhart/alpine-node:latest  
  
RUN apk add --update tini unzip  
  
ADD https://github.com/plouc/mozaik-demo/archive/master.zip /  
RUN unzip master.zip && \  
mv mozaik-demo-master mozaik  
  
WORKDIR /mozaik  
  
RUN npm install && \  
npm install mozaik-ext-jenkins && \  
npm install mozaik-ext-json && \  
npm install mozaik-ext-value && \  
npm run build-assets && \  
mv /mozaik/config.js /mozaik/config.js.bak  
  
VOLUME "/mozaik/config.js"  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 5000  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/bin/sh", "/entrypoint.sh"]  


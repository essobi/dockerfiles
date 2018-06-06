FROM node:carbon  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ENV OPENHIM_CORE_VERSION 4.0.1  
RUN curl -sL "https://github.com/jembi/openhim-core-
js/archive/v$OPENHIM_CORE_VERSION.tar.gz" | \  
tar --strip-components=1 -zxvf - && \  
npm install && \  
npm run build && \  
npm cache clean --force  
  
ENV NODE_ENV $NODE_ENV  
  
CMD ["node", "lib/server.js"]  


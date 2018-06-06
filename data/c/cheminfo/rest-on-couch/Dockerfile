FROM node:10-alpine  
  
ENV NODE_ENV production  
ENV REST_ON_COUCH_HOME_DIR /rest-on-couch  
  
ENV ROC_VERSION 5.6.1  
RUN apk add --no-cache curl && \  
curl -fSL https://github.com/cheminfo/rest-on-
couch/archive/v$ROC_VERSION.tar.gz -o $ROC_VERSION.tar.gz && \  
tar -xzf $ROC_VERSION.tar.gz && \  
mv rest-on-couch-${ROC_VERSION} rest-on-couch-source && \  
npm install -g pm2 && \  
cd /rest-on-couch-source && \  
NODE_ENV=development npm install && \  
npm run build && \  
npm install && \  
rm -rf /root/.npm /usr/local/share/.cache /root/.cache /${ROC_VERSION}.tar.gz
/rest-on-couch-source/test  
  
WORKDIR /rest-on-couch-source  
CMD ["node", "bin/rest-on-couch-server.js"]  


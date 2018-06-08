FROM mhart/alpine-node:4  
WORKDIR /src  
ADD . .  
  
# Run this all on one line to prevent build crud from being saved on
intermediary layers.  
RUN apk add --no-cache make gcc g++ python && \  
npm i -g gulp && \  
npm install --development && \  
gulp build && \  
npm prune --production && \  
npm cache clean && \  
apk del make gcc g++ python && \  
rm -rf /root/.node-gyp && \  
rm -rf /tmp/*  
  
ENV NODE_ENV production  
EXPOSE 3000  
CMD ["node", "index.js"]  


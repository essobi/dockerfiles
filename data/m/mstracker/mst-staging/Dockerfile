FROM node:6-slim  
  
WORKDIR /src  
ADD . .  
  
# Run this all on one line to prevent build crud from being saved on
intermediary layers.  
RUN npm i -g gulp && \  
npm install --development && \  
gulp build && \  
npm prune --production && \  
npm cache clean && \  
rm -rf /root/.node-gyp && \  
rm -rf /tmp/*  
  
ENV NODE_ENV production  
EXPOSE 3030  
CMD ["npm", "start"]  
  


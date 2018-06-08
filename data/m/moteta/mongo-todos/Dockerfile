FROM node:9-alpine  
RUN mkdir /todo  
COPY client /todo/client  
RUN cd /todo/client \  
&& yarn install \  
&& yarn run build --production \  
&& yarn run gzip-busybox  
  
  
  
FROM node:9-alpine  
RUN mkdir /todo  
COPY server /todo/server  
RUN cd /todo/server && yarn install && yarn run build  
  
  
  
FROM node:9-alpine  
RUN mkdir /todo  
COPY \--from=0 /todo/client/public /todo/client/public  
COPY \--from=1 /todo/server/dist /todo/server/dist  
COPY \--from=1 /todo/server/package.json /todo/server/yarn.lock
/todo/server/.babelrc /todo/server/  
WORKDIR /todo/server  
RUN yarn install --production  
ENV NODE_ENV=production  
  
CMD ["node", "dist/index.js"]  


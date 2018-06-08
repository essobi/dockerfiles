# This is the build stage.  
FROM node:8.1.3 as meego_backend  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm i  
RUN mkdir -p /meego/server && cp -a /tmp/node_modules /meego/server/  
WORKDIR /meego/server  
ADD . /meego/server/  
RUN npm run build  
  
# This is the execution stage.  
FROM node:8.1.3  
ADD package.json /tmp/package.json  
ENV NODE_ENV production  
RUN cd /tmp && npm i --production  
RUN mkdir -p /meego/server && cp -a /tmp/node_modules /meego/server/  
WORKDIR /meego/server  
COPY \--from=meego_backend /meego/server/_dist ./_dist  
COPY \--from=meego_backend /meego/server/config.json ./_dist/config.json  
COPY \--from=meego_backend /meego/server/assets ./assets  
COPY \--from=meego_backend /meego/server/package.json .  
COPY \--from=meego_backend /meego/server/views ./_dist/views  
RUN mkdir -p ./assets/images/nearby  
RUN mkdir -p ./assets/images/user  
RUN mkdir -p ./assets/images/guide  
RUN mkdir -p ./assets/images/guide_license  
CMD ["npm", "start"]  


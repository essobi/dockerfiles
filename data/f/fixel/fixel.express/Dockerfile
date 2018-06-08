FROM node:9-alpine AS build  
  
COPY package.json package.json  
COPY package-lock.json package-lock.json  
  
RUN npm install  
  
COPY public public  
COPY src src  
COPY server server  
COPY .babelrc .babelrc  
  
COPY webpack.config.production.js webpack.config.production.js  
COPY config/config.production.js config/config.production.js  
  
RUN npm run build  
  
FROM node:9-alpine  
COPY \--from=build /public /public  
  
COPY package.json package.json  
COPY src src  
COPY server server  
COPY .babelrc .babelrc  
COPY config/config.production.js config/config.production.js  
  
RUN npm install --production  
  
CMD npm run start  
  
EXPOSE 3300


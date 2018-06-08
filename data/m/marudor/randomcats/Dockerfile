FROM node:10-alpine as build  
WORKDIR /usr/app  
COPY package.json yarn.lock /usr/app/  
RUN yarn  
COPY src/ /usr/app/src/  
COPY .babelrc.js /usr/app/  
ENV NODE_ENV=production  
RUN yarn build  
  
FROM node:10-alpine  
  
RUN apk add --update-cache imagemagick  
  
RUN mkdir -p /usr/app  
WORKDIR /usr/app  
COPY package.json yarn.lock /usr/app/  
ENV NODE_ENV=production  
RUN yarn --prod  
COPY \--from=build /usr/app/lib /usr/app  
CMD ["node", "index.js"]  


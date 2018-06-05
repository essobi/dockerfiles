FROM node:8.9.4-alpine  
MAINTAINER koomrhythm@gmail.com  
  
RUN echo 'https://dl-3.alpinelinux.org/alpine/v3.6/main' >>
/etc/apk/repositories  
RUN apk update && apk upgrade  
RUN apk add --no-cache libpng-dev git  
  
# Prepare app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN npm install express  
ADD . /tmp  
  
# Build the app  
RUN cd /tmp && npm run build  
RUN cp -a /tmp/dist /usr/src/app  
ADD server.js /usr/src/app  
ADD package.json /usr/src/app  
RUN rm -rvf /tmp/*  
  
ENV NODE_ENV=production  
ENV PORT=8080  
# Expose the app port  
EXPOSE 8080  
# Start the app  
ENTRYPOINT ["npm", "run", "prod"]  


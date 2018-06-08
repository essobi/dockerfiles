FROM node:alpine  
  
MAINTAINER "Zoltan Simon" <hello@zoltansimon.me>  
LABEL vendor="Zoltan Simon <hello@zoltansimon.me>"  
LABEL description="Yeoman scaffolding that works!"  
LABEL version="0.2.0"  
  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
  
RUN npm install -g yo  
RUN npm cache clear  
RUN mkdir /yo  
RUN chown -R node:node /usr/local/lib/node_modules  
USER node  
  
WORKDIR /yo  
  
CMD ["yo", "--help"]  
  


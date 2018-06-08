FROM node:9.2.0-alpine  
MAINTAINER Robbert Klarenbeek <robbertkl@renbeek.nl>  
  
ARG NODE_ENV=production  
ENV NODE_ENV=${NODE_ENV}  
  
WORKDIR /usr/src/app  
  
RUN apk add --no-cache certbot nginx openssl  
COPY acme-challenge /etc/nginx/  
RUN rm -rf /var/www/*  
RUN openssl req \  
-x509 \  
-newkey rsa:2048 \  
-keyout /etc/ssl/private/snakeoil.key \  
-out /etc/ssl/certs/snakeoil.pem \  
-days 365 \  
-nodes \  
-subj "/CN=INVALID HOST"  
  
COPY package.json yarn.lock ./  
RUN [ "${NODE_ENV}"="production" ] && yarn install --frozen-lockfile
--production && yarn cache clean  
COPY . .  
  
VOLUME /etc/letsencrypt  
EXPOSE 80  
EXPOSE 443  
CMD [ "node", "." ]  


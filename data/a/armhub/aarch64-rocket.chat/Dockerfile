FROM resin/aarch64-alpine:3.6  
  
MAINTAINER Adrien Girardeau <adrigir25@gmail.com>  
  
RUN [ "cross-build-start" ]  
  
RUN apk add \--no-cache nodejs-current nodejs-current-npm curl  
  
RUN addgroup -S rocketchat && adduser -S -g rocketchat rocketchat \  
&& mkdir -p /app/uploads \  
&& chown rocketchat.rocketchat /app/uploads  
  
VOLUME /app/uploads  
  
ENV RC_VERSION 0.57.3  
  
WORKDIR /app  
  
RUN curl -fSL "https://rocket.chat/releases/${RC_VERSION}/download" -o
rocket.chat.tgz \  
&& tar zxf rocket.chat.tgz \  
&& rm rocket.chat.tgz rocket.chat.tgz.asc \  
&& apk del gnupg curl \  
&& cd bundle/programs/server \  
&& npm install  
  
USER rocketchat  
  
WORKDIR /app/bundle  
  
# needs a mongoinstance - defaults to container linking with alias 'db'  
ENV MONGO_URL=mongodb://db:27017/meteor \  
HOME=/tmp \  
PORT=3000 \  
ROOT_URL=http://localhost:3000 \  
Accounts_AvatarStorePath=/app/uploads  
  
RUN [ "cross-build-end" ]  
  
EXPOSE 3000  
  
CMD ["node", "main.js"]  


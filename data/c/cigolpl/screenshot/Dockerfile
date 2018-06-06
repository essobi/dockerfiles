FROM node:9-alpine  
  
RUN apk update  
RUN apk add --no-cache curl make gcc g++  
RUN apk add --no-cache linux-headers binutils-gold gnupg libstdc++  
RUN apk add --no-cache bash curl git nodejs yarn  
RUN apk add --update nodejs nodejs-npm && npm install npm@latest -g  
  
RUN apk update  
RUN apk add --no-cache bash curl fontconfig optipng zip  
  
RUN apk add curl \  
&& curl -Ls https://github.com/fgrehm/docker-
phantomjs2/releases/download/v2.0.0-20150722/dockerized-phantomjs.tar.gz \  
| tar xz -C /  
  
RUN apk add --no-cache bash curl  
  
RUN apk add imagemagick  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY package.json /app/  
ADD . /app  
  
RUN npm install  
#RUN yarn install  
EXPOSE 3000  
CMD ["node", "server.js"]  


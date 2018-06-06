FROM node:8-alpine  
  
WORKDIR /usr/src/JustMeme  
COPY package.json ./  
  
RUN apk add --update \  
&& apk add --no-cache --virtual .build-deps python gcc g++ make  
  
RUN npm i -g nodemon \  
&& npm i ffmpeg-binaries \  
&& npm install \  
&& apk del .build-deps  
  
COPY . .  
  
EXPOSE 4000  
CMD ["npm", "start"]


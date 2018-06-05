FROM wavebreakmedia/ffmpeg3.4.2-alpine3.6 AS builtffmpeg  
  
RUN apk add --no-cache --update expat  
  
FROM wavebreakmedia/node6.13-alpine3.6  
COPY \--from=builtffmpeg /usr/local /usr/local  
  
RUN apk add --update --no-cache \  
build-base \  
autoconf \  
bash \  
python \  
krb5-dev \  
graphicsmagick \  
libjpeg-turbo-dev \  
cairo-dev \  
imagemagick \  
icu-dev \  
jpeg-dev \  
libpng-dev \  
giflib-dev \  
pango-dev \  
giflib-dev \  
netcat-openbsd \  
gd-dev \  
git && \  
npm install pm2 -g  
  
ENV HOME=/home/app  
  
RUN mkdir -p $HOME/burrito  
COPY package.json $HOME/burrito  
  
WORKDIR $HOME/burrito  
RUN npm install --only=prod  
  


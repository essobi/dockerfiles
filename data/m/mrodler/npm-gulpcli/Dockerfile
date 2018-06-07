FROM node:alpine  
  
LABEL maintainer="Markus Rodler"  
  
RUN npm install -g gulp-cli \  
&& apk add --update --quiet --no-cache \  
automake \  
git \  
alpine-sdk \  
nasm \  
autoconf \  
build-base \  
zlib \  
zlib-dev \  
libpng \  
libpng-dev\  
libwebp \  
libwebp-dev \  
libjpeg-turbo \  
libjpeg-turbo-dev \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
VOLUME ["/workdir"]  
WORKDIR /workdir  
  
CMD ["npm", "-v"]


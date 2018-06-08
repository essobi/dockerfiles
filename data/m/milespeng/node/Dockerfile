FROM node:alpine  
  
LABEL maintainer="mingpeng16@gmail.com"  
# Fix "mozjpeg pre-build test failed", see
https://github.com/imagemin/imagemin/issues/168#issuecomment-265545957  
# But this will increase the image size  
RUN apk add --no-cache --virtual .build-deps \  
libpng-dev \  
autoconf \  
automake \  
make \  
g++ \  
libtool \  
nasm \  
&& rm -rf /tmp/*  
  
RUN npm install -g cnpm --registry=https://registry.npm.taobao.org


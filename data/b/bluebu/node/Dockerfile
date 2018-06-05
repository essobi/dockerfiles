FROM node:7-alpine  
MAINTAINER bluebu <bluebuwang@gmail.com>  
  
# https://docs.npmjs.com/getting-started/fixing-npm-permissions  
# ENV \  
# OPTIPNG_VERSION=0.7.5  
# NPM_CONFIG_PREFIX=/npm/global  
#------------------------------------------------------------------------------  
# Environment variables:  
#------------------------------------------------------------------------------  
RUN echo "@edge-community http://dl-cdn.alpinelinux.org/alpine/edge/community"
>> /etc/apk/repositories  
  
# libjpeg-turbo-utils openjpeg-dev libjpeg-turbo-dev freetype-dev
gifsicle@edge-community  
RUN apk --update --no-cache \  
add \  
tar bash openssh-client \  
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
libjpeg-turbo-utils \  
gifsicle@edge-community \  
optipng@edge-community \  
&& rm /var/cache/apk/*  
  
# optipng  
# && curl -L -O
http://downloads.sourceforge.net/project/optipng/OptiPNG/optipng-$OPTIPNG_VERSION/optipng-$OPTIPNG_VERSION.tar.gz
\  
# && tar zxf optipng-$OPTIPNG_VERSION.tar.gz \  
# && cd optipng-$OPTIPNG_VERSION \  
# && ./configure && make && make install \  
# && cd .. \  
# RUN mkdir -p /npm/global \  
# && npm install -g gifsicle jpegtran-bin optipng-bin gulp gulp-imagemin  
# RUN npm install -g gulp gulp-imagemin  
RUN npm install -g gulp gulp-imagemin  
RUN npm install -g gifsicle jpegtran-bin optipng-bin  
  
# RUN sudo chown -R $(whoami) $(npm config get prefix) \  
# && npm install -g gifsicle jpegtran-bin optipng-bin gulp gulp-imagemin


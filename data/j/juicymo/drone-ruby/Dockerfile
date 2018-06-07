# see https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/ for Dockerfile best practices  
# build me with:  
# docker build -t "juicymo/drone-ruby:2.4.2" .  
FROM alpine:3.6  
MAINTAINER Tomas Jukin <tomas.jukin@juicymo.cz>  
  
RUN apk add --no-cache ruby=2.4.2-r0 ruby-bundler ruby-dev  
  
ENV BUILD_PACKAGES curl-dev build-base bash  
ENV RUBY_PACKAGES cairo-dev postgresql-dev tzdata wget postgresql=9.6.5-r0  
ENV WKHTMLTOPDF_PACKAGES gtk+ glib ttf-freefont fontconfig dbus  
  
RUN apk add --no-cache \  
$BUILD_PACKAGES \  
$RUBY_PACKAGES \  
$WKHTMLTOPDF_PACKAGES \  
git \  
imagemagick \  
less \  
nodejs \  
nodejs-npm \  
openssh  
  
RUN wget --no-check-certificate https://github.com/kernix/wkhtmltopdf-docker-
alpine/raw/master/wkhtmltopdf -P /usr/bin/  
RUN chmod a+x /usr/bin/wkhtmltopdf  
  
ENV SHELL /bin/bash  
ENV LC_ALL en_US.UTF-8  
ENV LANG=en_US.UTF-8  
ENV LANGUAGE=en_US.UTF-8  
RUN gem install bundler --no-ri --no-rdoc  
RUN npm install -g yarn


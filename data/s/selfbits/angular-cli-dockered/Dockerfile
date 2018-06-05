FROM node:8-alpine  
MAINTAINER Klaus Welle <dev@selfbits.io>  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh nano  
  
RUN npm install npm@latest && \  
rm -rf /usr/local/lib/node_modules/npm && \  
mv node_modules/npm /usr/local/lib/node_modules/npm  
  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
rm -r /root/.cache  
  
RUN pip3 install awscli && aws --version  
RUN npm cache verify  
RUN npm i -g semver @ionic/cli-utils tslib chalk os-name glob inherits once
rimraf @ionic/discover  
RUN npm rebuild node-sass  
RUN npm i -g cordova  
RUN npm i -g ionic@latest && ionic --no-interactive config set -g
daemon.updates false  
RUN npm rebuild node-sass  
RUN npm i -g @angular/cli@1.6.1  
RUN npm rebuild node-sass && npm cache verify  
  
RUN apk add --no-cache curl  
  
RUN npm i -g glob inherits once rimraf @ionic/discover  
  
# Add patch fix for segmentation error when running ionic serve  
COPY stack-fix.c /lib/  
# Prepare the libraries packages  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps build-base \  
&& gcc -shared -fPIC /lib/stack-fix.c -o /lib/stack-fix.so \  
&& apk del .build-deps  
  
# export the environment variable of LD_PRELOAD  
ENV LD_PRELOAD /lib/stack-fix.so  
# JAVA OPEN JDK Installation  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u131  
ENV JAVA_ALPINE_VERSION 8.131.11-r2  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# Install ruby gem and cocoapods  
RUN apk update && apk upgrade && apk --update add \  
ruby ruby-irb ruby-rake ruby-io-console ruby-bigdecimal ruby-json ruby-bundler
\  
libstdc++ tzdata bash ca-certificates \  
&& echo 'gem: --no-document' > /etc/gemrc \  
&& gem install cocoapods --user-install \  
&& gem which cocoapods \  
&& sed -e '/help/s/^/#/g' -i
/root/.gem/ruby/2.4.0/gems/cocoapods-1.3.1/lib/cocoapods/command.rb  
  
ENV GEM_HOME /root/.gem  
ENV PATH /root/.gem/ruby/2.4.0/bin:$PATH  
  
RUN \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk --no-cache update \  
&& apk --no-cache upgrade \  
&& apk add --no-cache --virtual .build-deps \  
gifsicle pngquant optipng libjpeg-turbo-utils \  
udev ttf-opensans chromium \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
ENV CHROME_BIN /usr/bin/chromium-browser  
ENV LIGHTHOUSE_CHROMIUM_PATH /usr/bin/chromium-browser  


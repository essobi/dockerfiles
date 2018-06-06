# Dockerfile grantmacken/alpine-openresty  
# https://github.com/grantmacken/alpine-openresty  
FROM alpine:3.7 as packager  
LABEL maintainer="Grant Mackenzie <grantmacken@gmail.com>"  
ENV OPENRESTY_HOME /usr/local/openresty  
ENV OPENRESTY_BIN /usr/local/openresty/bin  
ENV INSTALL_PATH /grantmacken  
RUN mkdir -p $INSTALL_PATH  
WORKDIR $INSTALL_PATH  
COPY Makefile Makefile  
# build-base like build-essentials  
# contains make  
# First Stage:  
# this installs openresty from sources into /usr/local/openresty  
# the install build dependencies are the remove  
RUN apk add --no-cache --virtual .build-deps \  
build-base \  
linux-headers \  
cmake \  
grep \  
wget \  
curl \  
tar \  
perl-dev \  
perl-utils \  
gd-dev \  
readline-dev \  
&& mkdir tmp \  
&& make -j$(grep ^proces /proc/cpuinfo | wc -l) install \  
&& rm -rf tmp \  
&& apk del .build-deps  
  
# Second Stage: dev  
FROM alpine:3.7 as dev  
ENV OPENRESTY_HOME /usr/local/openresty  
ENV OPENRESTY_BIN /usr/local/openresty/bin  
WORKDIR $OPENRESTY_HOME  
COPY \--from=packager /usr/local /usr/local  
RUN apk add --no-cache \  
gd \  
geoip \  
libgcc \  
libxslt \  
perl \  
curl \  
&& mkdir -p /etc/letsencrypt/live \  
&& mkdir /home/t \  
&& mkdir /home/bin \  
&& ln -s $OPENRESTY_BIN/openresty /usr/local/bin \  
&& ln -s $OPENRESTY_BIN/openresty /usr/local/bin/nginx \  
&& ln -s $OPENRESTY_BIN/resty /usr/local/bin \  
&& ln -s /home/t $OPENRESTY_HOME \  
&& ln -sf /dev/stdout $OPENRESTY_HOME/nginx/logs/access.log \  
&& ln -sf /dev/stderr $OPENRESTY_HOME/nginx/logs/error.log  
  
ENV LANG C.UTF-8  
EXPOSE 80 443  
STOPSIGNAL SIGTERM  
ENTRYPOINT ["bin/openresty", "-g", "daemon off;"]  
  
# Third Stage: prod  
FROM alpine:3.7 as prod  
ENV OPENRESTY_HOME /usr/local/openresty  
ENV OPENRESTY_BIN /usr/local/openresty/bin  
COPY \--from=packager /usr/local/openresty /usr/local/openresty  
COPY \--from=packager /usr/local/lib/lib* /usr/local/lib/  
WORKDIR $OPENRESTY_HOME  
RUN apk add --no-cache \  
gd \  
geoip \  
libgcc \  
libxslt \  
&& mkdir -p /etc/letsencrypt/live \  
&& ln -s $OPENRESTY_BIN/openresty /usr/local/bin \  
&& ln -sf /dev/stdout $OPENRESTY_HOME/nginx/logs/access.log \  
&& ln -sf /dev/stderr $OPENRESTY_HOME/nginx/logs/error.log  
  
ENV LANG C.UTF-8  
EXPOSE 80 443  
STOPSIGNAL SIGTERM  
ENTRYPOINT ["bin/openresty", "-g", "daemon off;"]  
  
# DEV notes:  
# home/t is for the 'prove' tests dir  
# home/bin is the for 'resty cli'  
# not sure about keeping  
# libxslt \  
# geoip \  


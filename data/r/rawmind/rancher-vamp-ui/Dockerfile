FROM rawmind/alpine-nginx:0.0.1-1  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# Compile and install vamp-ui  
ENV VAMP_UI_VERSION=0.8.4 \  
VAMP_UI_REPO=https://github.com/magneticio/vamp-ui.git \  
VAMP_UI_DIR=/opt/src/vamp-ui  
  
RUN apk add --update nodejs git python make gcc g++ \  
&& mkdir -p /opt/src; cd /opt/src \  
&& git clone -b "$VAMP_UI_VERSION" ${VAMP_UI_REPO} \  
&& cd ${VAMP_UI_DIR} \  
&& npm install \  
&& npm install gulp \  
&& npm i -g gulp \  
&& gulp build \  
&& cd / && cp -rp ${VAMP_UI_DIR}/build/* /opt/www/ \  
&& apk del nodejs git python make gcc g++ \  
&& rm -rf /var/cache/apk/* /opt/src  
  
# Adding files  
ADD root /  


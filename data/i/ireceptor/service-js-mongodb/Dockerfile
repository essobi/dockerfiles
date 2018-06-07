# Base Image  
FROM ubuntu:16.04  
LABEL maintainer.first="VDJServer <vdjserver@utsouthwestern.edu>" \  
maintainer.second="iReceptor <ireceptor@sfu.ca>"  
  
# PROXY: uncomment these if building behind UTSW proxy  
#ENV http_proxy 'http://proxy.swmed.edu:3128/'  
#ENV https_proxy 'https://proxy.swmed.edu:3128/'  
#ENV HTTP_PROXY 'http://proxy.swmed.edu:3128/'  
#ENV HTTPS_PROXY 'https://proxy.swmed.edu:3128/'  
# Install OS Dependencies  
RUN DEBIAN_FRONTEND='noninteractive' apt-get update &&
DEBIAN_FRONTEND='noninteractive' apt-get install -y \  
make \  
wget \  
xz-utils \  
default-jre \  
git  
  
##################  
##################  
# not currently using redis and supervisor  
# old stuff  
# nodejs \  
# nodejs-legacy \  
# npm \  
# redis-server \  
# redis-tools \  
# sendmail-bin \  
# supervisor \  
# Setup postfix  
# The postfix install won't respect noninteractivity unless this config is set
beforehand.  
#RUN mkdir /etc/postfix  
#RUN touch /etc/mailname  
#COPY docker/postfix/main.cf /etc/postfix/main.cf  
#COPY docker/scripts/postfix-config-replace.sh /root/postfix-config-replace.sh  
# Debian vociferously complains if you try to install postfix and sendmail at
the same time.  
#RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y -q --force-yes \  
# postfix  
##################  
##################  
# node  
RUN wget https://nodejs.org/dist/v8.9.0/node-v8.9.0-linux-x64.tar.xz  
RUN tar xf node-v8.9.0-linux-x64.tar.xz  
RUN cp -rf /node-v8.9.0-linux-x64/bin/* /usr/local/bin  
RUN cp -rf /node-v8.9.0-linux-x64/lib/* /usr/local/lib  
RUN cp -rf /node-v8.9.0-linux-x64/include/* /usr/local/include  
RUN cp -rf /node-v8.9.0-linux-x64/share/* /usr/local/share  
  
RUN npm install -g swagger  
  
RUN mkdir /service-js-mongodb  
RUN mkdir /service-js-mongodb/ireceptor-node  
  
# PROXY: More UTSW proxy settings  
#RUN npm config set proxy http://proxy.swmed.edu:3128  
#RUN npm config set https-proxy http://proxy.swmed.edu:3128  
# Install npm dependencies (optimized for cache)  
COPY ireceptor-node/package.json /service-js-mongodb/ireceptor-node  
RUN cd /service-js-mongodb/ireceptor-node && npm install  
  
# pull in sway bug fix for array parameters  
RUN cd /service-js-mongodb/ireceptor-node && npm install
https://github.com/apigee-127/sway.git#94ba34f --save  
  
# Setup redis  
#COPY docker/redis/redis.conf /etc/redis/redis.conf  
# Setup supervisor  
#COPY docker/supervisor/supervisor.conf /etc/supervisor/conf.d/  
# Copy project source  
COPY . /service-js-mongodb  
RUN cp /service-js-mongodb/api/iReceptor_Data_Service_API_V2.json /service-js-
mongodb/ireceptor-node/api/swagger/iReceptor_Data_Service_API_V2.json  
  
# Copy AIRR spec  
RUN cp /service-js-mongodb/airr-standards/specs/definitions.yaml /service-js-
mongodb/ireceptor-node/config/airr-definitions.yaml  
  
CMD ["node", "--harmony", "/service-js-mongodb/ireceptor-node/app.js"]  


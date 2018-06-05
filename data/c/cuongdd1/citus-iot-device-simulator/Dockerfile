FROM alpine:3.6  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
COPY . /data  
WORKDIR /data  
  
ENV DEVICE_ID= SECRET_KEY= INSTALL_ALL=NO INSTALL_DOCKER=NO  
  
# bower requires this configuration parameter to allow bower install using
root.  
RUN echo '{ "allow_root": true }'>.bowerrc  
RUN mkdir -p /root/.agent/ && touch /root/.agent/update.log  
  
# node-sass doesn't support Alpine, so we need the build toolchain.  
RUN apk --update add curl ca-certificates wget python3 py-requests && update-
ca-certificates &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /data  
  
CMD crond && tail -f /root/.agent/update.log  
  


FROM orbweb/node:4.4.3  
MAINTAINER Orbweb Inc. <engineering@orbweb.com>  
  
ENV VERSION 1.2.0  
WORKDIR /  
RUN apk --no-cache add --virtual .build-deps \  
build-base \  
python \  
zeromq-dev && \  
npm install -g \  
mosca@$VERSION \  
bunyan@1.5.1 \  
leveldown@1.4.3 \  
zmq@2.14.0 \  
amqp@0.2.4 \  
redis@2.5.0 \  
hiredis@0.4.1 \  
mongodb@2.1.4 && \  
apk del .build-deps  
VOLUME ["/db"]  
EXPOSE 80/tcp 443/tcp 1883/tcp 8883/tcp  
CMD mosca -v -d /db -p 1883 --http-port 80 | bunyan  


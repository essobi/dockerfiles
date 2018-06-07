FROM mvertes/alpine-mongo:latest  
MAINTAINER Dave Finster <df@docketbook.io>  
  
ENV CONTAINERBUDDY_VERSION 1.2.1  
  
COPY mongodb-consul.json /etc/mongodb-consul.json  
COPY mongodb_health.sh /usr/local/bin/mongodb_health.sh  
  
USER root  
  
RUN set -x \  
&& apk add --no-cache --virtual .build-deps \  
openssl \  
&& wget -O containerbuddy.tar.gz
https://github.com/joyent/containerbuddy/releases/download/"$CONTAINERBUDDY_VERSION"/containerbuddy-"$CONTAINERBUDDY_VERSION".tar.gz
\  
&& tar -xzf containerbuddy.tar.gz -C /usr/local/bin \  
&& rm -r containerbuddy.tar.gz \  
&& apk del .build-deps \  
&& chmod +x /usr/local/bin/mongodb_health.sh  
  
ENV CONTAINERBUDDY=file:///etc/mongodb-consul.json  
  
EXPOSE 27017 28017  
  
ENTRYPOINT [ "/usr/local/bin/containerbuddy", "mongod"]


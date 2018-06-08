FROM node:8.6.0-alpine  
MAINTAINER Vlad Poenaru <vlad.wing@gmail.com>  
COPY src/package.json src/yarn.lock /srv/statsd/  
RUN apk add --no-cache --virtual .build-deps \  
binutils-gold \  
findutils \  
curl \  
g++ \  
gcc \  
make \  
git \  
rsync && apk add --no-cache python zeromq-dev \  
&& cd /srv/statsd \  
&& yarn global add node-gyp \  
&& yarn install \  
&& mkdir -p /tmp/statsd \  
&& git clone https://github.com/etsy/statsd.git /tmp/statsd \  
&& rsync -av /tmp/statsd/ /srv/statsd && rm -rf /tmp/statsd \  
&& apk del .build-deps  
  
ENV DOCKERIZE_VERSION v0.6.0  
RUN apk add --no-cache openssl \  
&& wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz \  
&& rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
COPY src/config.js.tmpl src/statsd.sh /srv/statsd/  
COPY src/jcatascopia.js /srv/statsd/backends/  
EXPOSE 8125/udp  
CMD ["dockerize", "-template",
"/srv/statsd/config.js.tmpl:/srv/statsd/config.js", "/srv/statsd/statsd.sh"]  


FROM python:2.7.12-alpine  
  
MAINTAINER Stefan Negru <stefan.negru@helsinki.fi>  
  
RUN apk add --update \  
&& apk add --no-cache build-base \  
&& apk add --no-cache linux-headers \  
&& apk add --no-cache bash \  
&& apk add --no-cache py-setuptools \  
&& rm -rf /var/cache/apk/*  
  
ENV GOSU_VERSION 1.10  
RUN set -x \  
&& apk add --no-cache --virtual .gosu-deps \  
dpkg \  
gnupg \  
openssl \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apk del .gosu-deps  
  
RUN pip install --upgrade pip  
RUN pip install browsepy  
  
RUN addgroup -S nonroot \  
&& adduser -S -g nonroot nonroot  
  
COPY entrypoint.sh /  
  
RUN mkdir files \  
&& chmod +x /entrypoint.sh  
  
# setting environment variables for entrypoint script  
# setting also directories to be owned by the nonroot user  
ENV GOSU_USER nonroot:nonroot  
ENV GOSU_CHOWN /files  
  
VOLUME ["/files"]  
  
EXPOSE 5050  
ENTRYPOINT ["/entrypoint.sh", "--directory", "/files"]  


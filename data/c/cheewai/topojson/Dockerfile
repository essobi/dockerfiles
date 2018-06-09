# 2017-11-01 Tagged to 8 and not latest (9+) because NPM does not support 9
yet!  
#2018-02-09 FROM mhart/alpine-node:8  
FROM mhart/alpine-node:9  
LABEL maintainer "Cheewai Lai <clai@csir.co.za>"  
  
ARG GOSU_VERSION=1.10  
ARG GOSU_PATH=/usr/bin/gosu  
  
# DO NOT npm install -g restify  
RUN apk update \  
&& apk add curl python2 \  
&& curl -o $GOSU_PATH -sSL
https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64 \  
&& chmod +x $GOSU_PATH \  
&& npm install -g topojson \  
&& npm install restify \  
&& apk del curl \  
&& rm -rf /var/cache/apk/*  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  


FROM node:8-alpine  
MAINTAINER Tomoyuki Sugimura <tomoyuki.sugimura@gmail.com>  
  
ARG version=5.4.0.0  
EXPOSE 8080  
WORKDIR /opt/es-sql-site-standalone  
RUN apk update \  
&& apk add --no-cache --virtual .builddeps wget ca-certificates openssl \  
&& wget https://github.com/NLPchina/elasticsearch-
sql/releases/download/${version}/es-sql-site-standalone.zip \  
&& apk del --purge .builddeps \  
&& unzip es-sql-site-standalone.zip \  
&& rm es-sql-site-standalone.zip \  
&& cd site-server \  
&& npm install express --save  
  
WORKDIR site-server  
USER nobody  
ENTRYPOINT ["node", "node-server.js"]  


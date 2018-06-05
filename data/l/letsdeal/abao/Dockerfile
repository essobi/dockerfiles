FROM node:7-alpine  
  
RUN apk add --no-cache openssl  
  
ENV DOCKERIZE_VERSION v0.4.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz \  
&& rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
RUN npm install -qg abao@~0.4 \  
&& npm cache clean  
  
RUN mkdir -p /data  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["abao"]  
  
CMD ["--help"]  


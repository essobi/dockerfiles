FROM node:alpine  
  
ENV BRANCH "master"  
RUN apk add --no-cache openssl \  
&& wget https://github.com/remyla/damas-core/archive/${BRANCH}.zip \  
&& unzip ${BRANCH}.zip \  
&& rm ${BRANCH}.zip \  
&& ln -s /damas-core-${BRANCH}/server-nodejs/ /data \  
&& npm install --prefix /data/ \  
&& apk del openssl  
  
VOLUME /data  
  
WORKDIR /damas-core-${BRANCH}/server-nodejs/  
  
EXPOSE 8090 8443  
CMD ["node","."]  


FROM alpine  
MAINTAINER garrett@garrettboast.com  
  
ENV CONFIG_FLAGS=""  
ENV DEFAULT_MAX_MONGO_VERSION=3.5  
EXPOSE 27017  
RUN addgroup -S mongodb && adduser -S -G mongodb mongodb  
  
#RUN mkdir /docker-entrypoint-initdb.d  
RUN mkdir -p /data/db /data/configdb \  
&& chown -R mongodb:mongodb /data/db /data/configdb  
  
RUN apk add --no-cache \  
"mongodb<${MONGO_VERSION:-$DEFAULT_MAX_MONGO_VERSION}" \  
bash \  
jq \  
ca-certificates \  
&& apk add --no-cache gosu --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /var/lib/mongodb \  
&& mv /etc/conf.d/mongodb /etc/conf.d/mongodb.orig  
  
VOLUME /data/db /data/configdb  
  
COPY docker-entrypoint.sh /bin/  
  
RUN ln -s /bin/docker-entrypoint.sh /entrypoint.sh ; chmod a+x /bin/docker-
entrypoint.sh ; mkdir /docker-entrypoint-initdb.d /docker-entrypoint-post-
setup.d  
  
COPY initdb.d/* /docker-entrypoint-initdb.d/  
COPY post-setup.d/* /docker-entrypoint-post-setup.d/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["mongod"]  


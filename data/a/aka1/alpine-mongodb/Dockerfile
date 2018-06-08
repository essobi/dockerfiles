FROM alpine:latest  
  
RUN addgroup -S mongodb && adduser -Sg mongodb mongodb  
  
RUN set -x \  
&& echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk update \  
&& apk add -u --no-cache \  
bash \  
jq \  
mongodb \  
numactl@testing \  
su-exec \  
&& rm -rf /var/lib/mongodb  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN mkdir -p /data/db /data/configdb \  
&& chown -R mongodb:mongodb /data/db /data/configdb  
VOLUME /data/db /data/configdb  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backward compatibility  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 27017  
CMD ["mongod"]  


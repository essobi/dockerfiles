FROM bitnami/minideb  
  
ENV MONGO_MAJOR 3.4  
ENV MONGO_VERSION 3.4.1  
ENV MONGO_PACKAGE mongodb-org  
  
COPY ./tools/docker-entrypoint /entrypoint.sh  
COPY ./tools/suexec.bin /usr/local/bin/suexec  
  
RUN echo "\033[36m === Install MongoDB $MONGO_VERSION === \033[0m" \  
&& set -x \  
&& echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-
org/$MONGO_MAJOR main" > /etc/apt/sources.list.d/mongodb-org.list \  
&& apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
0C49F3730359A14518585931BC711F9BA15703C6 \  
&& install_packages \  
numactl \  
${MONGO_PACKAGE}=$MONGO_VERSION \  
${MONGO_PACKAGE}-server=$MONGO_VERSION \  
${MONGO_PACKAGE}-shell=$MONGO_VERSION \  
${MONGO_PACKAGE}-mongos=$MONGO_VERSION \  
${MONGO_PACKAGE}-tools=$MONGO_VERSION \  
&& (groupadd -r mongodb || true) \  
&& (useradd -r -g mongodb mongodb || true) \  
&& mv /etc/mongod.conf /etc/mongod.conf.orig \  
&& mkdir -p /data/db /data/configdb \  
&& chown -R mongodb:mongodb /data/db /data/configdb \  
&& chmod +x /entrypoint.sh /usr/local/bin/suexec \  
&& rm -rf /var/lib/mongodb  
  
VOLUME ["/data/db", "/data/configdb"]  
EXPOSE 27017  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mongod"]  


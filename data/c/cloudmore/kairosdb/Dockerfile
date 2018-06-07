FROM alpine:3.5  
EXPOSE 8080 4242 2003 2004  
ARG APK_CACHE_IP=172.17.0.1  
ARG APK_CACHE_DOMAIN='dl-cdn.alpinelinux.org'  
ARG RUN_DEPS='su-exec openjdk8-jre openssl bash gettext'  
ARG BUILD_DEPS='tar coreutils'  
#ARG KAIROSDB_VERSION=1.1.2  
ARG KAIROSDB_URL='https://github.com/kairosdb/kairosdb/releases'  
#ARG KAIROS_CARBON_VERSION=1.1  
ARG KAIROS_CARBON_URL='https://github.com/kairosdb/kairos-carbon/releases'  
ENV KAIROSDB_HOME=/opt/kairosdb  
ENV KAIROSDB_CONF=$KAIROSDB_HOME/conf  
ENV PATH=$KAIROSDB_HOME/bin:$PATH  
  
RUN nc -z $APK_CACHE_IP 80 && echo $APK_CACHE_IP $APK_CACHE_DOMAIN
>>/etc/hosts \  
; apk --update add --no-cache $RUN_DEPS $BUILD_DEPS \  
&& mkdir -p $KAIROSDB_HOME && cd $KAIROSDB_HOME \  
&& KAIROSDB_LATEST=$(wget -qO- $KAIROSDB_URL | egrep -o
"v[0-9]+\\.[0-9]+\\.[0-9]+" | sort -Vr | head -1 | cut -d "v" -f 2) \  
&& echo "Installing KairosDB ${KAIROSDB_VERSION:=$KAIROSDB_LATEST}" \  
&& wget -O-
$KAIROSDB_URL/download/v${KAIROSDB_VERSION}/kairosdb-${KAIROSDB_VERSION}-1.tar.gz
| tar xz --strip-components=1 \  
&& sed -i
's|^kairosdb.service.datastore=.*$|kairosdb.service.datastore=org.kairosdb.datastore.cassandra.CassandraModule|'
$KAIROSDB_CONF/kairosdb.properties \  
&& sed -i
's|^kairosdb.datastore.cassandra.host_list=.*$|kairosdb.datastore.cassandra.host_list=localhost:9160|'
$KAIROSDB_CONF/kairosdb.properties \  
&& KAIROS_CARBON_LATEST=$(wget -qO- $KAIROS_CARBON_URL | egrep -o
"v[0-9]+\\.[0-9]+-" | sort -Vr | head -1 | cut -d "v" -f 2 | cut -d "-" -f 1)
\  
&& echo "Installing kairos-carbon
${KAIROS_CARBON_VERSION:=$KAIROS_CARBON_LATEST}" \  
&& wget -O- $KAIROS_CARBON_URL/download/v${KAIROS_CARBON_VERSION}-1/kairos-
carbon-${KAIROS_CARBON_VERSION}.tar.gz | tar xz --strip-components=1 \  
&& apk del $BUILD_DEPS && rm -rf /var/cache/apk/*  
  
WORKDIR $KAIROSDB_HOME  
  
ADD . .  
  
VOLUME $KAIROSDB_HOME/data $KAIROSDB_HOME/log $KAIROSDB_HOME/build /tmp  
  
CMD ["kairosdb.sh", "run"]  


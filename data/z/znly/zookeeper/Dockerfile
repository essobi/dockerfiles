FROM progrium/busybox  
MAINTAINER jbaptiste <jb@zen.ly>  
  
# Java options, heap memory and used version  
ENV JAVA_HOME /opt/jre1.8.0_40  
ENV JVM_HEAP_MEMORY "1g"  
# Specific zookeeper options for this image  
ENV ZOOKEEPER_VERSION 3.4.8  
ENV ZOO_SERVERS "zookeeper1"  
ENV ZOO_ID "1"  
ENV ZOO_DATA_DIR "/data/zookeeper"  
# Install Java oracle, zookeeper and cleanup unnecessary files  
RUN opkg-install wget bash tar \  
&& wget -q --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" -O - \  
http://download.oracle.com/otn-pub/java/jdk/8u40-b26/jre-8u40-linux-x64.tar.gz
| tar -xzf - -C /opt \  
&& ln -sf /lib/libpthread-2.18.so /lib/libpthread.so.0 \  
&& ln -s /opt/jre1.8.0_40/bin/java /usr/bin/java \  
&& rm -rf /opt/jre1.8.0_40/plugin \  
/opt/jre1.8.0_40/bin/javaws \  
/opt/jre1.8.0_40/bin/jjs \  
/opt/jre1.8.0_40/bin/keytool \  
/opt/jre1.8.0_40/bin/orbd \  
/opt/jre1.8.0_40/bin/pack200 \  
/opt/jre1.8.0_40/bin/policytool \  
/opt/jre1.8.0_40/bin/rmid \  
/opt/jre1.8.0_40/bin/rmiregistry \  
/opt/jre1.8.0_40/bin/servertool \  
/opt/jre1.8.0_40/bin/tnameserv \  
/opt/jre1.8.0_40/bin/unpack200 \  
/opt/jre1.8.0_40/lib/javaws.jar \  
/opt/jre1.8.0_40/lib/deploy* \  
/opt/jre1.8.0_40/lib/desktop \  
/opt/jre1.8.0_40/lib/*javafx* \  
/opt/jre1.8.0_40/lib/*jfx* \  
/opt/jre1.8.0_40/lib/amd64/libdecora_sse.so \  
/opt/jre1.8.0_40/lib/amd64/libprism_*.so \  
/opt/jre1.8.0_40/lib/amd64/libfxplugins.so \  
/opt/jre1.8.0_40/lib/amd64/libglass.so \  
/opt/jre1.8.0_40/lib/amd64/libgstreamer-lite.so \  
/opt/jre1.8.0_40/lib/amd64/libjavafx*.so \  
/opt/jre1.8.0_40/lib/amd64/libjfx*.so \  
/opt/jre1.8.0_40/lib/ext/jfxrt.jar \  
/opt/jre1.8.0_40/lib/ext/nashorn.jar \  
/opt/jre1.8.0_40/lib/oblique-fonts \  
/opt/jre1.8.0_40/lib/plugin.jar\  
&& wget -q -O -
http://apache.mirrors.ovh.net/ftp.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-${ZOOKEEPER_VERSION} /opt/zookeeper \  
&& mkdir -p ${ZOO_DATA_DIR}  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 2181 2888 3888  
ENTRYPOINT ["/docker-entrypoint.sh"]  


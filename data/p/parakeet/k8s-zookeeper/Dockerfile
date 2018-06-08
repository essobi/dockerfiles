FROM ubuntu:16.04  
  
ENV ZK_USER=zk \  
ZK_HOME=/zk \  
ZK_DATA_DIR=/var/lib/zookeeper/data \  
ZK_DATALOG_DIR=/var/lib/zookeeper/log \  
ZK_LOG_DIR=/var/log/zookeeper  
  
ARG ZK_DIST=zookeeper-3.5.3-beta  
  
RUN set -x pipefail \  
&& apt-get update \  
&& apt-get install -y openjdk-8-jre-headless wget netcat-openbsd \  
&& wget \--quiet
"http://www.apache.org/dist/zookeeper/$ZK_DIST/$ZK_DIST.tar.gz" \  
&& wget \--quiet
"http://www.apache.org/dist/zookeeper/$ZK_DIST/$ZK_DIST.tar.gz.asc" \  
&& wget \--quiet "http://www.apache.org/dist/zookeeper/KEYS" \  
&& export GNUPGHOME="$(mktemp --directory)" \  
&& gpg \--import KEYS \  
&& gpg \--batch --verify "$ZK_DIST.tar.gz.asc" "$ZK_DIST.tar.gz" \  
&& tar \--extract --file="$ZK_DIST.tar.gz" \--directory=/opt \  
&& ln -s /opt/$ZK_DIST /opt/zookeeper \  
&& rm --recursive --force "$GNUPGHOME" "$ZK_DIST.tar.gz" "$ZK_DIST.tar.gz.asc"
\  
&& rm --recursive --force /opt/zookeeper/CHANGES.txt \  
/opt/zookeeper/README.txt \  
/opt/zookeeper/NOTICE.txt \  
/opt/zookeeper/CHANGES.txt \  
/opt/zookeeper/README_packaging.txt \  
/opt/zookeeper/build.xml \  
/opt/zookeeper/config \  
/opt/zookeeper/contrib \  
/opt/zookeeper/dist-maven \  
/opt/zookeeper/docs \  
/opt/zookeeper/ivy.xml \  
/opt/zookeeper/ivysettings.xml \  
/opt/zookeeper/recipes \  
/opt/zookeeper/src \  
/opt/zookeeper/$ZK_DIST.jar.asc \  
/opt/zookeeper/$ZK_DIST.jar.md5 \  
/opt/zookeeper/$ZK_DIST.jar.sha1 \  
&& apt-get autoremove -y wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Copy configuration generator and setup scripts to bin and make executable  
COPY zkGenConfig.sh zkOK.sh zkMetrics.sh "/opt/zookeeper/bin/"  
  
# Create a user for the zookeeper process and configure file system ownership  
# for nessecary directories and modify scripts as a user executable  
RUN set -x \  
&& useradd $ZK_USER \  
&& [ `id -u $ZK_USER` -eq 1000 ] \  
&& [ `id -g $ZK_USER` -eq 1000 ] \  
&& mkdir -p $ZK_DATA_DIR $ZK_DATA_LOG_DIR $ZK_LOG_DIR /usr/share/zookeeper
/tmp/zookeeper /usr/etc/ \  
&& chown -R "$ZK_USER:$ZK_USER" /opt/$ZK_DIST $ZK_DATA_DIR $ZK_LOG_DIR
$ZK_DATA_LOG_DIR /tmp/zookeeper \  
&& chmod ugo+x /opt/zookeeper/bin/* \  
&& ln -s /opt/zookeeper/conf/ /usr/etc/zookeeper \  
&& ln -s /opt/zookeeper/bin/* /usr/bin \  
&& ln -s /opt/zookeeper/$ZK_DIST.jar /usr/share/zookeeper/ \  
&& ln -s /opt/zookeeper/lib/* /usr/share/zookeeper  
WORKDIR /opt/zookeeper/bin


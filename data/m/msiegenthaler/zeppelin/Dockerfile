FROM java:openjdk-8-jdk  
  
ENV VERSION=0.5.6  
# Add Tini  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "-g", "--"]  
  
# Add Gosu  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
RUN groupadd zeppelin && \  
useradd -d /opt/zeppelin -g zeppelin -s /bin/bash zeppelin  
  
RUN . /etc/profile && \  
mkdir -p /opt && \  
echo "Downloading.." && \  
wget -q
http://mirror.switch.ch/mirror/apache/dist/incubator/zeppelin/${VERSION}-incubating/zeppelin-${VERSION}-incubating-
bin-all.tgz -O /opt/zeppelin.tgz && \  
echo "Extracting.." && \  
tar -xzf /opt/zeppelin.tgz -C /opt && \  
ln -s /opt/zeppelin-${VERSION}-incubating-bin-all /opt/zeppelin && \  
chown -R zeppelin:zeppelin /opt/zeppelin-${VERSION}-incubating-bin-all && \  
rm /opt/zeppelin.tgz  
  
RUN mkdir -p /opt/zeppelin/logs && \  
chown zeppelin:zeppelin /opt/zeppelin/logs && \  
mkdir -p /opt/zeppelin/run && \  
chown zeppelin:zeppelin /opt/zeppelin/run  
  
RUN mkdir -p /data && \  
chown zeppelin:zeppelin /data  
  
ADD start-zeppelin.sh /  
  
EXPOSE 8080  
VOLUME ["/opt/zeppelin/notebook", "/data"]  
  
CMD [ "/start-zeppelin.sh" ]  


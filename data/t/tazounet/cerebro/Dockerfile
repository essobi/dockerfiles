FROM openjdk:8-jre  
  
ENV GOSU_VERSION 1.10  
ENV CEREBRO_VERSION 0.6.5  
  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
# && gpg \--keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& cd /opt/ \  
&& wget -O cerebro-${CEREBRO_VERSION}.tgz
https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz
\  
&& mkdir -p /opt/cerebro \  
&& tar zxvf cerebro-${CEREBRO_VERSION}.tgz -C /opt/cerebro --strip-
components=1 \  
&& rm cerebro-${CEREBRO_VERSION}.tgz \  
&& groupadd cerebro && useradd -g cerebro cerebro \  
&& chown cerebro:cerebro -R /opt/cerebro \  
&& wget -O /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd \  
&& mkdir -p /etc/confd/{conf.d,templates}  
  
COPY files/application.toml /etc/confd/conf.d/application.toml  
COPY files/application.conf.tmpl /etc/confd/templates/application.conf.tmpl  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
WORKDIR /opt/cerebro  
  
EXPOSE 9000  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  


FROM openjdk:7-jre-alpine  
  
ENV DUMB_INIT_VERSION 1.2.0  
RUN set -ex \  
&& apk add --no-cache --virtual .install-deps openssl \  
&& wget "https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64" \  
&& wget "https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/sha256sums" \  
&& grep "dumb-init_${DUMB_INIT_VERSION}_amd64$" sha256sums | sha256sum -c \  
&& rm sha256sums \  
&& mv dumb-init_${DUMB_INIT_VERSION}_amd64 /usr/bin/dumb-init \  
&& chmod +x /usr/bin/dumb-init \  
&& apk del .install-deps  
  
ENV ACTIVEMQ_VERSION 5.14.4  
RUN set -ex \  
&& adduser -D -u 1000 activemq \  
&& activemq_name=apache-activemq-${ACTIVEMQ_VERSION} \  
&& activemq_archive=${activemq_name}-bin.tar.gz \  
&& apk add --no-cache su-exec \  
&& apk add --no-cache --virtual .install-deps gnupg openssl tar \  
&& wget
https://archive.apache.org/dist/activemq/${ACTIVEMQ_VERSION}/${activemq_archive}
\  
&& wget
https://archive.apache.org/dist/activemq/${ACTIVEMQ_VERSION}/${activemq_archive}.asc
\  
&& wget https://www.apache.org/dist/activemq/KEYS \  
&& gpg --import KEYS \  
&& gpg --batch --verify ${activemq_archive}.asc ${activemq_archive} \  
&& mkdir -p /opt/activemq \  
&& tar xzf ${activemq_archive} \  
-C /opt/activemq \  
\--strip-components=1 \  
\--exclude='*examples*' \  
\--exclude='*docs*' \  
\--exclude='*webapps-demo*' \  
&& rm ${activemq_archive} ${activemq_archive}.asc KEYS \  
&& apk del .install-deps \  
&& rm -rf /root/.gnupg  
  
COPY log4j.properties /opt/activemq/conf/log4j.properties  
COPY etc_default_activemq /etc/default/activemq  
COPY run.sh /run.sh  
  
# openwire stomp ws amqp mqtt admin  
EXPOSE 61616 61613 61614 5672 1883 8161  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["/run.sh"]  


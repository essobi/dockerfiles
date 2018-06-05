FROM java:7  
MAINTAINER John Paul Alcala, jpalcala@ayannah.com  
  
# Taken from Postgres Official Dockerfile.  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
ENV ACTIVEMQ_VERSION="5.13.2" \  
ACTIVEMQ_HOME="/usr/local/activemq" \  
ACTIVEMQ_BASE="/var/lib/activemq" \  
ACTIVEMQ_OPTS_MEMORY="-Xms256M -Xmx256M"  
RUN groupadd -g 1000 activemq && \  
useradd -g activemq -u 1000 -r -M activemq && \  
mkdir -p $ACTIVEMQ_HOME && \  
curl -SL http://www.apache.org/dist/activemq/KEYS -o /tmp/KEYS && \  
curl -SL http://archive.apache.org/dist/activemq/$ACTIVEMQ_VERSION/apache-
activemq-$ACTIVEMQ_VERSION-bin.tar.gz -o /tmp/apache-activemq.tar.gz && \  
curl -SL http://archive.apache.org/dist/activemq/$ACTIVEMQ_VERSION/apache-
activemq-$ACTIVEMQ_VERSION-bin.tar.gz.asc -o /tmp/apache-activemq.tar.gz.asc
&& \  
gpg --import /tmp/KEYS && \  
gpg --verify /tmp/apache-activemq.tar.gz.asc && \  
tar xzf /tmp/apache-activemq.tar.gz -C $ACTIVEMQ_HOME \--strip-components=1 &&
\  
chmod -R a+r /usr/local/activemq && \  
ln -s /usr/local/activemq/bin/activemq /usr/local/bin/activemq && \  
rm -rf /tmp/* && \  
mkdir -p $ACTIVEMQ_BASE/data && cp -rf $ACTIVEMQ_HOME/conf $ACTIVEMQ_BASE  
  
COPY activemq-entrypoint.sh /  
  
EXPOSE 61616 5672 61613 1883 61614 8161  
VOLUME ["/var/lib/activemq/data"]  
  
ENTRYPOINT ["/activemq-entrypoint.sh"]  
  
CMD ["activemq"]  


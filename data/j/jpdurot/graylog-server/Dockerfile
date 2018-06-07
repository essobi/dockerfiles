FROM java:8-jre  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre  
ENV GRAYLOG_SERVER_JAVA_OPTS "-Xms1g -Xmx2g -XX:NewRatio=1
-XX:MaxMetaspaceSize=256m -server -XX:+ResizeTLAB -XX:+UseConcMarkSweepGC
-XX:+CMSConcurrentMTEnabled -XX:+CMSClassUnloadingEnabled -XX:+UseParNewGC
-XX:-OmitStackTraceInFastThrow"  
ENV GOSU_VERSION 1.7  
RUN set -x \  
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
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https \  
&& wget
https://packages.graylog2.org/repo/packages/graylog-2.1-repository_latest.deb
\  
&& dpkg -i graylog-2.1-repository_latest.deb \  
&& apt-get update \  
&& apt-get install -y graylog-server \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
ENV ELASTICSEARCH_VERSION 2.4.0  
ENV ELASTICSEARCH_REPO_BASE
http://packages.elasticsearch.org/elasticsearch/2.x/debian  
  
RUN echo "deb $ELASTICSEARCH_REPO_BASE stable main" >
/etc/apt/sources.list.d/elasticsearch.list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends
elasticsearch=$ELASTICSEARCH_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y python-setuptools \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN easy_install supervisor  
  
ENV PATH /usr/share/graylog-server/bin:/usr/share/elasticsearch/bin:$PATH  
  
WORKDIR /usr/share/elasticsearch  
  
RUN set -ex \  
&& for path in \  
./data \  
./logs \  
./config \  
./config/scripts \  
; do \  
mkdir -p "$path"; \  
chown -R elasticsearch:elasticsearch "$path"; \  
done  
  
COPY config_es ./config  
  
WORKDIR /usr/share/graylog-server  
  
RUN set -ex \  
&& for path in \  
./data/journal \  
./data/log \  
./data/config \  
; do \  
mkdir -p "$path"; \  
done  
  
COPY config_graylog ./data/config  
COPY supervisord.conf /etc/supervisord.conf  
COPY docker-entrypoint.sh /  
  
RUN chmod u+x /docker-entrypoint.sh  
  
VOLUME /usr/share/elasticsearch/data  
  
EXPOSE 9000 12900  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]


FROM java:8-jre  
MAINTAINER nicolaihald  
  
# grab gosu for easy step-down from root  
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
  
# https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-
repositories.html  
# https://packages.elasticsearch.org/GPG-KEY-elasticsearch  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
ENV ELASTICSEARCH_MAJOR 2.3  
ENV ELASTICSEARCH_VERSION 2.3.3  
ENV ELASTICSEARCH_REPO_BASE
http://packages.elasticsearch.org/elasticsearch/2.x/debian  
ENV ES_HOME /usr/share/elasticsearch  
  
RUN echo "deb $ELASTICSEARCH_REPO_BASE stable main" >
/etc/apt/sources.list.d/elasticsearch.list  
  
###############################################################################  
# CONFIGURATION  
###############################################################################  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends
elasticsearch=$ELASTICSEARCH_VERSION \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
ENV PATH ${ES_HOME}/bin:$PATH  
  
# install plugins  
RUN ${ES_HOME}/bin/plugin install cloud-aws --timeout 2m && \  
${ES_HOME}/bin/plugin install royrusso/elasticsearch-HQ --timeout 2m  
  
# set working directory and create directories  
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
  
###############################################################################  
# DATA  
###############################################################################  
  
# Configure environment  
COPY root/ /  
RUN chmod +x /docker-entrypoint.sh  
  
  
###############################################################################  
# EXPOSE & VOLUMES  
###############################################################################  
VOLUME ["${ES_HOME}"]  
#VOLUME /usr/share/elasticsearch  
#VOLUME /usr/share/elasticsearch/data  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport/cluster  
EXPOSE 9200 9300  
  
###############################################################################  
# START  
###############################################################################  
  
# Start container  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["elasticsearch"]  


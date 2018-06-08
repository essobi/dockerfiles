FROM java:8-jre  
MAINTAINER nicolaihald  
# TODO: Merge RUN and ENV commands (fewer layers)  
# install plugin dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libzmq3 \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# the "ffi-rzmq-core" gem is very picky about where it looks for libzmq.so  
RUN mkdir -p /usr/local/lib \  
&& ln -s /usr/lib/*/libzmq.so.3 /usr/local/lib/libzmq.so  
  
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
  
# https://www.elastic.co/guide/en/logstash/2.3/package-repositories.html  
# https://packages.elastic.co/GPG-KEY-elasticsearch  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
ENV LOGSTASH_MAJOR 2.3  
ENV LOGSTASH_VERSION 1:2.3.2-1  
ENV LOGSTASH_HOME /opt/logstash  
ENV PATH $LOGSTASH_HOME/bin:$PATH  
  
RUN echo "deb http://packages.elastic.co/logstash/${LOGSTASH_MAJOR}/debian
stable main" > /etc/apt/sources.list.d/logstash.list  
  
RUN set -x \  
&& mkdir -p /config \  
&& mkdir -p /data \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends logstash=$LOGSTASH_VERSION \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Support downloading logstash configuration file during container startup:  
ENV LOGSTASH_CFG_URL=""  
# ENV
LOGSTASH_CFG_URL="https://raw.githubusercontent.com/nicolaihald/dockerfiles/master/logstash/logstash.searchlogger.conf"  
# # update geolite database  
# RUN set -x \  
# && mkdir -p /data/geoip \  
# && mkdir -p /config \  
# # Download latest version of the geolite database  
# && wget -q -O /tmp/GeoLiteCity.dat.gz
"http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz" \  
# && gzip -d /tmp/GeoLiteCity.dat.gz > /data/geoip/GeoLiteCity.dat \  
# && rm /tmp/GeoLiteCity.dat \  
# ## Set owner of logstash home so we can access the  
# && chown -hR logstash:logstash /data/geoip \  
# && chmod -R 777 /data/geoip  
# install plugins  
RUN $LOGSTASH_HOME/bin/logstash-plugin install logstash-input-beats  
  
#WORKDIR $LOGSTASH_HOME  
COPY root/ /  
RUN chmod +x /start.sh && chown -hR logstash:logstash /start.sh  
  
# /conf is the default directory where our logstash will read pipeline config
files  
# /logs is an optional attach point to reference something like /var/log on
the host  
VOLUME ["/config","/data"]  
  
# Listen for defaults: 25826 (collectd), 5044 (beats)  
EXPOSE 25826 5044  
ENTRYPOINT ["/start.sh"]  
#CMD ["bin/logstash", "agent", "-f","/config"]  
CMD ["-e", ""]  
  


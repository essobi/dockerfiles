FROM docker.elastic.co/logstash/logstash:6.2.4  
LABEL maintainer="Ilija Vukotic <ivukotic@cern.ch>"  
  
RUN mkdir /usr/share/logstash/rucio  
RUN mkdir /usr/share/logstash/pilot  
RUN mkdir /usr/share/logstash/xcache_atlasrift  
RUN mkdir /usr/share/logstash/stashcp  
  
RUN mkdir /usr/share/logstash/templates  
  
RUN curl -O
"http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz"  
RUN gunzip GeoLite2-City.mmdb.gz  
  
RUN bin/logstash-plugin install logstash-input-stomp  
  
COPY logstash.yml /usr/share/logstash/config/  
COPY pipelines.yml /usr/share/logstash/config/  
  
COPY pipelines/rucio-events.conf /usr/share/logstash/rucio/  
COPY pipelines/PandaPilot.conf /usr/share/logstash/pilot/  
COPY pipelines/ATLASrift.conf pipelines/xCacheMonitoringCollector.conf
pipelines/x1t-jobs.conf /usr/share/logstash/xcache_atlasrift/  
COPY pipelines/StashCP.conf /usr/share/logstash/stashcp/  
  
COPY templates/ATLASrift.template /usr/share/logstash/templates/


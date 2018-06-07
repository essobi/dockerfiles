FROM java:8-jre  
  
ENV ES_PKG_NAME elasticsearch-2.2.0  
# explicitly set user/group IDs  
RUN groupadd -r elasticsearch --gid=888 && useradd -r -g elasticsearch
--uid=888 elasticsearch  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
RUN apt-get update && apt-get -y install python3-requests  
  
RUN \  
cd / && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz
&& \  
tar xvzf $ES_PKG_NAME.tar.gz && \  
rm -f $ES_PKG_NAME.tar.gz && \  
mv /$ES_PKG_NAME /elasticsearch  
  
COPY elasticsearch.yml.template
/elasticsearch/config/elasticsearch.yml.template  
#COPY run.sh /elasticsearch/run.sh  
COPY template_syslog.json /elasticsearch/config/templates/template_syslog.json  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 9200  
EXPOSE 9300  
CMD ["elasticsearch"]  


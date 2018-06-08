FROM ubuntu:16.04  
MAINTAINER Elastic Docker Team <docker@elastic.co>  
  
ARG ELASTIC_VERSION=6.1.0  
ARG
LOGSTASH_DOWNLOAD_URL=https://artifacts.elastic.co/downloads/logstash/logstash-${ELASTIC_VERSION}.tar.gz  
#ARG LOGSTASH_PACK_URL  
ARG
GEODB_DOWNLOAD_URL=http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz  
ARG ELASTICSEARCH_URL=elasticsearch  
  
# Install curl for downloading, Java for running Logstash/JRuby, and netbase  
# to resolve a warning from JRuby
(https://github.com/jruby/jruby/issues/3955).  
RUN apt-get -qq update && \  
apt-get -qq install -y curl netbase openjdk-8-jdk-headless locales && \  
apt-get -qq clean  
  
# Provide a non-root user to run the process.  
RUN addgroup --gid 1000 logstash && \  
adduser --disabled-password \--gecos=logstash \--uid=1000 \--gid=1000 \  
\--home /usr/share/logstash --no-create-home logstash  
  
# Add Logstash itself.  
RUN curl -Lso - ${LOGSTASH_DOWNLOAD_URL} | \  
tar zxf - -C /usr/share && \  
mv /usr/share/logstash-${ELASTIC_VERSION} /usr/share/logstash && \  
chown --recursive logstash:logstash /usr/share/logstash/ && \  
ln -s /usr/share/logstash /opt/logstash  
ENV PATH=/usr/share/logstash/bin:$PATH  
  
# Add GeoLite2-City database  
RUN curl -Lso - ${GEODB_DOWNLOAD_URL} | \  
tar zxf - -C /usr/share && \  
mv /usr/share/Geo*/GeoLite2-City.mmdb /usr/share/logstash  
  
# Provide a minimal configuration, so that simple invocations will provide  
# a good experience.  
ADD config/logstash.yml config/log4j2.properties /usr/share/logstash/config/  
ADD pipeline /usr/share/logstash/pipeline/  
ADD templates /usr/share/logstash/templates/  
  
RUN chown --recursive logstash:logstash /usr/share/logstash/config/
/usr/share/logstash/pipeline/ /usr/share/logstash/templates/  
  
# Ensure Logstash has a UTF-8 locale available.  
RUN locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LC_ALL='en_US.UTF-8'  
ADD bin/docker-entrypoint.sh /usr/share/logstash/bin/docker-entrypoint.sh  
RUN chmod +x /usr/share/logstash/bin/docker-entrypoint.sh  
  
USER logstash  
  
RUN cd /usr/share/logstash/bin && logstash-plugin install logstash-filter-
translate  
  
EXPOSE 9600 5044  
  
ENTRYPOINT ["/usr/share/logstash/bin/docker-entrypoint.sh"]  
CMD ["-f", "/usr/share/logstash/pipeline/"]  


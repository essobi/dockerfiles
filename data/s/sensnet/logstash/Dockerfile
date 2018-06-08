FROM docker.elastic.co/logstash/logstash:5.4.2  
# install plugins  
RUN cd /usr/share/logstash \  
&& logstash-plugin install logstash-input-beats \  
&& logstash-plugin install logstash-output-elasticsearch  
  
USER root  
  
# https://github.com/elastic/logstash-docker/issues/38  
ADD docker-entrypoint /usr/local/bin/  
RUN chmod 0755 /usr/local/bin/docker-entrypoint  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]  
  
# For geoip filter  
#RUN cd /tmp \  
# && wget -q
http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz \  
# && tar -xzf GeoLite2-City.tar.gz --strip-components=1 \  
# && cp GeoLite2-City.mmdb /etc/logstash/GeoLite2-City.mmdb  
# && rm -rf *  
COPY logstash.yml /opt/logstash/  
COPY conf.d/*.conf /opt/logstash/conf.d/  
COPY patterns/ /opt/logstash/patterns/  
  
#USER logstash  
# https://www.elastic.co/guide/en/logstash/current/command-line-flags.html  
CMD [ "logstash", "--path.settings", "/opt/logstash/logstash.yml", "--
path.config", "/opt/logstash/conf.d" ]  


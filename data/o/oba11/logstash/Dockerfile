FROM java:7-jre  
MAINTAINER Oluwaseun Obajobi <oba@obajobi.com>  
  
ENV LOGSTASH_VERSION 2.0.0  
# Download Logstash Package  
ADD
https://download.elastic.co/logstash/logstash/logstash-${LOGSTASH_VERSION}.tar.gz
/tmp/logstash.tar.gz  
RUN tar -xzvf /tmp/logstash.tar.gz && \  
mv /logstash-${LOGSTASH_VERSION} /opt/logstash && \  
rm -rf /tmp/*  
  
# Download GeoIP Database  
ADD
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
/usr/share/GeoIP/GeoIP.dat.gz  
ADD http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
/usr/share/GeoIP/GeoLiteCity.dat.gz  
RUN cd /usr/share/GeoIP && \  
zcat -f GeoIP.dat.gz > GeoIP.dat && \  
zcat -f GeoLiteCity.dat.gz > GeoIPCity.dat && \  
rm -rf /usr/share/GeoIP/*.gz  
  
# Copy Patterns  
COPY patterns/* /opt/logstash/patterns/  
  
# Copy Templates  
COPY templates /opt/logstash/templates  
  
VOLUME ["/etc/logstash"]  
  
ENTRYPOINT ["/opt/logstash/bin/logstash"]  
CMD ["agent", "-f", "/etc/logstash/logstash.conf"]  


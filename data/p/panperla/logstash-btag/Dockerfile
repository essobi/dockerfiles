# Logstash autobuild with maxmind geoip db  
# I need to use derviated container with ssl generated  
FROM logstash  
MAINTAINER maciej.perlinski@meant4.com  
  
# Automatic update and upgrade of packages every build  
RUN apt-get update && apt-get install -y  
  
# Downloading Maxmind's GEOIP database  
RUN wget -O -
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz | gunzip
-c > /etc/logstash/conf.d/GeoLiteCity.dat  
  
RUN mkdir -p /etc/pki/tls/certs  
RUN mkdir -p /etc/pki/tls/private  
  
# Finally copying our latest version of logstash.conf  
COPY logstash.conf /etc/logstash/conf.d/logstash.conf  
COPY logstash-forwarder.crt /etc/pki/tls/certs/logstash-forwarder.crt  
COPY logstash-forwarder.key /etc/pki/tls/private/logstash-forwarder.key  
COPY logstash-template.json /etc/logstash/conf.d/logstash-template.json


FROM sebp/elk  
  
RUN apt-get update \  
&& apt-get -y install python-pip \  
&& apt-get -y upgrade \  
&& pip install elasticsearch-curator \  
&& apt-get -y autoremove \  
&& apt-get -y autoclean  
  
EXPOSE 5044  
  
# Remove existing logstash configuration  
RUN rm /etc/logstash/conf.d/*  
  
# Add Logstash configuration  
ADD 0001-beats-input.conf /etc/logstash/conf.d/0001-beats-input.conf  
ADD 5001-squid-filter.conf /etc/logstash/conf.d/5001-squid-filter.conf  
ADD 9001-logstash-output.conf /etc/logstash/conf.d/9001-logstash-output.conf  
  
RUN mkdir -p /usr/share/GeoIP \  
&& curl -sSL
http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz -o
/usr/share/GeoIP/GeoLite2-City.tar.gz \  
&& tar xzvf /usr/share/GeoIP/GeoLite2-City.tar.gz --strip-components=1 -C
/usr/share/GeoIP \  
&& rm /usr/share/GeoIP/COPYRIGHT.txt /usr/share/GeoIP/GeoLite2-City.tar.gz
/usr/share/GeoIP/LICENSE.txt  


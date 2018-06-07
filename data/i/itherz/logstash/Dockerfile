FROM docker.elastic.co/logstash/logstash:5.5.2  
MAINTAINER Dmitrii Zolotov <dzolotov@herzen.spb.ru>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN cd /usr/share/logstash && curl -O
"http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz" &&
gunzip GeoLite2-City.mmdb.gz && \  
sed -i 's/0x78,0x../0x78,0x01/ig'
/usr/share/logstash/vendor/bundle/jruby/1.9/gems/gelfd-0.2.0/lib/gelfd.rb  
  
ADD elasticsearch-template.json /usr/share/logstash/templates/elasticsearch-
template.json  
  
ADD ./*.pattern /usr/share/logstash/patterns/  
ADD ./nginx /usr/share/logstash/patterns/  
  
ADD *.conf /etc/logstash/conf.d/  
  
EXPOSE 5000 5044 12201/udp 12202/udp  
  
CMD [ "-f", "/etc/logstash/conf.d/" ]  


FROM shift/java:8  
  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
WORKDIR /srv  
RUN apt-get install wget \  
&& wget http://download.elastic.co/logstash/logstash/logstash-1.5.0.tar.gz \  
&& tar xfvz logstash-1.5.0.tar.gz \  
&& mv logstash-1.5.0 logstash \  
&& rm logstash-1.5.0.tar.gz \  
&& /srv/logstash/bin/plugin install logstash-input-log-courier \  
&& /srv/logstash/bin/plugin install logstash-output-log-courier \  
&& /srv/logstash/bin/plugin install logstash-filter-geoip \  
&& /srv/logstash/bin/plugin install logstash-filter-mutate \  
&& /srv/logstash/bin/plugin install logstash-output-slack \  
&& /srv/logstash/bin/plugin install logstash-codec-json \  
&& /srv/logstash/bin/plugin install logstash-codec-plain \  
&& /srv/logstash/bin/plugin install logstash-filter-date \  
&& /srv/logstash/bin/plugin install logstash-output-influxdb \  
&& /srv/logstash/bin/plugin install logstash-output-riemann \  
&& ln -s /lib/x86_64-linux-gnu/libcrypt.so.1 /usr/lib/x86_64-linux-
gnu/libcrypt.so  
  
VOLUME /srv/logstash/config  
ADD files/start.sh /start.sh  
ENTRYPOINT ["/start.sh"]  
  
EXPOSE 9292  
EXPOSE 5425  
EXPOSE 6543/udp  
  


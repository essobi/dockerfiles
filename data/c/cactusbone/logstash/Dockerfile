FROM java:8  
MAINTAINER F4 <dev@f4-group.com>  
  
# Install dependencies  
RUN apt-get update  
RUN apt-get install -y wget git  
#install logstash  
RUN wget -q
https://download.elastic.co/logstash/logstash/logstash-2.4.1.tar.gz -O
/tmp/logstash.tar.gz && \  
(cd /tmp && tar zxf logstash.tar.gz && mv logstash-2.4.1 /opt/logstash && rm
logstash.tar.gz)  
RUN sed -i 's|kramdown.*|kramdown (1.14.0)|'
/opt/logstash/Gemfile.jruby-1.9.lock  
  
ADD run.sh /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
RUN git clone -b plugin-api-v1 --depth 1 https://github.com/F4-Group/logstash-
input-gelf.git /custom/logstash-input-gelf  
RUN sed -i 's|gem "logstash-input-gelf".*$|gem "logstash-input-gelf", :path =>
"/custom/logstash-input-gelf"|' /opt/logstash/Gemfile  
  
#install stuff for logstash-filter-geoip  
RUN git clone -b plugin-api-v1 --depth 1 https://github.com/F4-Group/logstash-
filter-geoip.git /custom/logstash-filter-geoip  
RUN sed -i 's|gem "logstash-filter-geoip".*$|gem "logstash-filter-geoip",
:path => "/custom/logstash-filter-geoip"|' /opt/logstash/Gemfile  
  
WORKDIR /custom/logstash-filter-geoip  
  
RUN wget -q https://s3.amazonaws.com/jruby.org/downloads/1.7.26/jruby-
bin-1.7.26.tar.gz -O /tmp/jruby.tar.gz && \  
(cd /tmp && tar zxf jruby.tar.gz && mv jruby-1.7.26 /opt/jruby && rm
jruby.tar.gz)  
RUN /opt/jruby/bin/jruby -S gem install bundler  
RUN /opt/jruby/bin/jruby -S bundle install --standalone  
RUN /opt/jruby/bin/jruby -S bundle exec rake vendor  
RUN /opt/jruby/bin/jruby -S bundle exec rake install_jars  
  
WORKDIR /  
#end logstash-filter-geoip  
RUN /opt/logstash/bin/logstash-plugin install --no-verify  
  
ADD logstash.conf.template /opt/logstash.conf.template  
  
#syslog  
EXPOSE 514  
#gelf udp  
EXPOSE 12201/udp  
  
#log4j  
EXPOSE 9500  
CMD ["/usr/local/bin/run"]  


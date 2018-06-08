FROM ruby:2  
MAINTAINER Secret Sauce Partners, Inc. <dev@sspinc.io>  
  
ENV REDIS_PLUGIN_VERSION 1.0.1  
RUN cd /tmp && \  
wget -q
https://github.com/kenjij/newrelic_redis_plugin/archive/v$REDIS_PLUGIN_VERSION.tar.gz
&& \  
mkdir /opt/newrelic_redis_plugin && \  
tar xzvf v$REDIS_PLUGIN_VERSION.tar.gz -C /opt/newrelic_redis_plugin --strip 1
&& \  
cd /opt/newrelic_redis_plugin && \  
bundle install && \  
rm /tmp/*  
  
COPY config/ /etc/newrelic_redis_plugin/  
  
CMD ["/opt/newrelic_redis_plugin/newrelic_redis_agent", "-c",
"/etc/newrelic_redis_plugin/newrelic_plugin.yml"]  


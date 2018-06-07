#  
# Rocketgraph logstash server  
#  
# Pull base image.  
FROM logstash:1.5.2  
MAINTAINER Konstantinos Christofilos <kostas.christofilos@rocketgraph.com>  
  
ADD ./nginx-access.pattern /logstash-patterns/nginx-access  
ADD ./nginx-error.pattern /logstash-patterns/nginx-error  
ADD ./monolog.pattern /logstash-patterns/monolog  
  
# Install supervisor  
RUN \  
apt-get update && \  
apt-get install -y supervisor  
  
ADD ./supervisor_logstash.conf /etc/supervisor/conf.d/supervisor_logstash.conf  
ADD ./logstash.conf /config-dir/logstash.conf  
  
ADD ./start.sh /start.sh  
RUN chmod a+x /start.sh  
  
CMD ["/start.sh"]


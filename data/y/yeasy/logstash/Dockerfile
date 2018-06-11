# This will prepare a logstash with netflow supported.  
# The logstash can be started with `logstash agent -f /etc/logstash/conf.d/`,
which will use the logstash_netflow.conf as the configuration file.  
FROM logstash:1.5  
MAINTAINER Baohua Yang  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY logstash_netflow.conf /etc/logstash/conf.d/  
  
RUN /opt/logstash/bin/plugin install --no-verify logstash-codec-netflow  


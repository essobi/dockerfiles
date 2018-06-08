FROM logstash:2-alpine  
MAINTAINER Vincent Ambo <vincent@nordcloud.com>  
  
WORKDIR /opt/logstash  
EXPOSE 8600  
# Add nginx pattern grok filter.  
ADD nginx /opt/logstash/patterns/nginx  
  
# Install log-courier input  
# https://github.com/driskell/log-
courier/blob/master/docs/LogstashIntegration.md  
RUN bin/plugin install logstash-input-courier  
  
# Add logstash configuration  
ADD logstash.conf /etc/logstash.conf  
  
# Override command  
CMD ["logstash", "agent", "-f", "/etc/logstash.conf"]  


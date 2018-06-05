FROM logstash:5.2.2-alpine  
MAINTAINER Evin Callahan <gaieges@gmail.com>  
  
# Copy build files to container root  
ADD . /app  
  
# Add any other plugins you need here  
RUN logstash-plugin install logstash-output-gelf logstash-output-syslog  
  
# Start logstash  
ENTRYPOINT ["/app/entrypoint.sh"]  


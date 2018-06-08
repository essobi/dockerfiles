FROM mastodonc/basejava  
  
RUN curl -sL https://download.elastic.co/logstash/logstash/logstash-all-
plugins-2.1.0.tar.gz | \  
tar -xzf - -C / --transform 's@\\([a-z-]*\\)-[0-9\\.]*@\1@'  
  
ADD logstash.conf /logstash/logstash.conf  
ADD start-logstash.sh /start-logstash  
  
# 4560 - socker appender for logback (keep in sync with logstash.conf  
# 4560 - socker appender for log4j (keep in sync with logstash.conf  
# 9092 - web interface to logstash.  
EXPOSE 4560 4561 9092  
# Start logstash  
CMD ["/bin/bash", "/start-logstash"]  


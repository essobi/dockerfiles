FROM logstash  
RUN logstash-plugin install logstash-output-syslog  
RUN logstash-plugin install logstash-output-influxdb  
RUN logstash-plugin install logstash-input-jdbc  
  
RUN wget -q -O /tmp/sqljdbc_6.0.8112.100_fra.tar.gz
https://download.microsoft.com/download/F/0/4/F045B371-3B6B-4816-BE96-651D29B4346C/fra/sqljdbc_6.0.8112.100_fra.tar.gz  
RUN cd /tmp && tar -xvzf /tmp/sqljdbc_6.0.8112.100_fra.tar.gz  
RUN find /tmp/ -type f -name "*.jar" -exec cp '{}' /usr/share/logstash/ ';'  
RUN find /usr/share/logstash/ -type f -name "sqljdbc*.jar" -exec chmod 444
'{}' ';'  
RUN find /usr/share/logstash/ -type f -name "sqljdbc*.jar" -exec chown
logstash:logstash '{}' ';'  
RUN rm -rf /tmp/sqljdbc*  
  


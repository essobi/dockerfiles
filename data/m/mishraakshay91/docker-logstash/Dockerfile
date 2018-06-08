FROM logstash:5  
MAINTAINER mishra.akshay91@gmail.com  
ADD logs/iis.log /var/log/iis.log  
expose 5044  
# Add your logstash plugins setup here  
# Example: RUN logstash-plugin install logstash-filter-json  
RUN logstash-plugin install logstash-input-beats  


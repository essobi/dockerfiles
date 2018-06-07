FROM logstash:1  
  
RUN apt-get update && apt-get install -y git && apt-get clean  
  
# Plugins for all. Installed from RubyGems  
RUN /opt/logstash/bin/plugin install logstash-filter-translate  
RUN /opt/logstash/bin/plugin install logstash-filter-useragent  
RUN /opt/logstash/bin/plugin install logstash-filter-geoip  
RUN /opt/logstash/bin/plugin install logstash-filter-ruby  
RUN /opt/logstash/bin/plugin install logstash-filter-cidr  
  


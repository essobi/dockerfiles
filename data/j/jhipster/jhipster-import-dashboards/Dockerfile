FROM docker.elastic.co/beats/metricbeat:6.2.2  
COPY dashboards /tmp  
WORKDIR /usr/share/metricbeat/  
COPY wait-for-elasticsearch.sh ./  
ENV ELASTICSEARCH_URL=http://jhipster-elasticsearch:9200  
ENV KIBANA_URL=http://jhipster-console:5601  
  
CMD ./wait-for-elasticsearch.sh && ./metricbeat setup --dashboards -E
output.elasticsearch.hosts="[$ELASTICSEARCH_URL]" -E
setup.kibana.host=$KIBANA_URL -E setup.dashboards.directory=/tmp


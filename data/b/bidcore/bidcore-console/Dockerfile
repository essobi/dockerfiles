FROM docker.elastic.co/kibana/kibana:6.1.3  
  
ENV ELASTICSEARCH_URL=http://bidcore-elasticsearch:9200  
COPY kibana.yml /usr/share/kibana/config/kibana.yml  
COPY bidconsole.svg /tmp/bidconsole.svg  
RUN ./bin/kibana-plugin install
https://github.com/sivasamyk/logtrail/releases/download/v0.1.25/logtrail-6.1.3-0.1.25.zip  
COPY logtrail.json /usr/share/kibana/plugins/logtrail/logtrail.json  


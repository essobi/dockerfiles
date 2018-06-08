FROM docker.elastic.co/kibana/kibana:5.4.2  
RUN set -ex \  
&& bin/kibana-plugin remove x-pack \  
&& bin/kibana-plugin install
https://github.com/sivasamyk/logtrail/releases/download/v0.1.15/logtrail-5.4.2-0.1.15.zip  
  
COPY logtrail.json ./plugins/logtrail/logtrail.json  


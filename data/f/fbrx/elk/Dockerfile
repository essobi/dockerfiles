FROM fbrx/java  
MAINTAINER Florian Brüssel <florian@florian-m.net>  
  
WORKDIR /opt  
  
#download binaries  
RUN wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.2.tar.gz  
RUN wget
https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz  
RUN wget https://download.elasticsearch.org/logstash/logstash/logstash-
contrib-1.4.2.tar.gz  
RUN wget https://download.elasticsearch.org/kibana/kibana/kibana-3.1.2.tar.gz  
  
#extract  
RUN tar -xzf elasticsearch*.tar.gz  
RUN tar -xzf logstash-1*.tar.gz  
RUN tar -xzf logstash-contrib*.tar.gz  
RUN tar -xzf kibana*.tar.gz  
  
#remove archives  
RUN rm *.tar.gz  
  
#CONFIG elasticsearch  
#install elastisearch plugin  
RUN elasticsearch-1.4.2/bin/plugin -install lmenezes/elasticsearch-kopf  
#add config  
ADD conf/elasticsearch.yml /opt/elasticsearch-1.4.2/config/  
  
#CONFIG kibana  
#install and configure nginx for kibana  
RUN apt-get install nginx -y  
ADD conf/nginx.kibana.conf /etc/nginx/sites-available/  
ADD conf/server.* /etc/nginx/ssl/  
RUN ln -s /etc/nginx/sites-available/nginx.kibana.conf /etc/nginx/sites-
enabled && rm /etc/nginx/sites-enabled/default  
ADD conf/kibana.config.js /opt/kibana-3.1.2/config.js  
ADD conf/AccessLogs.json /opt/kibana-3.1.2/app/dashboards/  
  
#CONFIG logstash  
ADD conf/logstash.elk.conf /opt/logstash-1.4.2/conf/  
  
#adding custom configs on build  
ONBUILD COPY * /opt/tmpconfig/  
ONBUILD RUN if [ -e /opt/tmpconfig/logstash.*.conf ]; then cp
/opt/tmpconfig/logstash.*.conf /opt/logstash-1.4.2/conf/; fi  
ONBUILD RUN if [ -e /opt/tmpconfig/server.* ]; then cp /opt/tmpconfig/server.*
/etc/nginx/ssl/; fi  
  
#add volume for external logs  
VOLUME /opt/logs  
  
#EXPOSE nginx  
EXPOSE 443  
#add entrypoint  
ADD docker_entrypoint.sh /  
ENTRYPOINT ["/docker_entrypoint.sh"]  


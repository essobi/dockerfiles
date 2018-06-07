FROM sebp/elk  
ADD ./03-udp-input.conf /etc/logstash/conf.d/03-udp-input.conf  
RUN echo "http.cors.enabled : true" >> /etc/elasticsearch/elasticsearch.yml  
RUN echo "http.cors.allow-origin: \"*\"" >>
/etc/elasticsearch/elasticsearch.yml  
ADD ./kibana-default-index.json /usr/local/bin/kibana-default-index.json  
ADD ./kibana-default-index-pattern.json /usr/local/bin/kibana-default-index-
pattern.json  
ADD ./scriptstoinsert.txt /usr/local/bin/scriptstoinsert.txt  
ADD ./init.sh /usr/local/bin/init.sh  
SHELL ["/bin/bash", "-c"]  
RUN . /usr/local/bin/init.sh  
EXPOSE 5601 9200 5044 5000 9998  
EXPOSE 5959/udp  
CMD [ "/usr/local/bin/start.sh" ]  


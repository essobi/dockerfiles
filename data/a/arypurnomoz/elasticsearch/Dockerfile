FROM arypurnomoz/java  
  
ADD
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.2.zip
/tmp/elastic.zip  
  
WORKDIR /tmp  
  
RUN \  
unzip /tmp/elastic.zip \  
&& rm /tmp/elastic.zip \  
&& mv /tmp/elastic* /es \  
&& chmod a+x /es/bin/* \  
&& /es/bin/plugin --install lmenezes/elasticsearch-kopf/master \  
&& /es/bin/plugin --install mobz/elasticsearch-head  
  
ADD run.sh /tmp/run.sh  
  
EXPOSE 9200 9300  
ENTRYPOINT ["/tmp/run.sh"]  


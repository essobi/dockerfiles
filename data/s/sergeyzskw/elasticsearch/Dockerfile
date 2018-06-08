FROM elasticsearch:2.4  
MAINTAINER Sergey Z <sergey.zsv.w@gmail.com>  
  
ENV ES_CFG /etc/elasticsearch/elasticsearch.yml  
  
RUN cd /usr/share/elasticsearch && \  
bin/plugin install mobz/elasticsearch-head && \  
bin/plugin install analysis-phonetic && \  
bin/plugin install analysis-icu && \  
echo >> $ES_CFG && \  
echo "script.inline: on" >> $ES_CFG && \  
echo "script.indexed: on" >> $ES_CFG  
  


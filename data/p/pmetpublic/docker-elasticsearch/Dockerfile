FROM elasticsearch:2.4.5  
MAINTAINER Keith Bentrup <kbentrup@magento.com>  
  
RUN bin/plugin install analysis-phonetic && \  
bin/plugin install analysis-icu && \  
echo -e "script.inline: on\nscript.inline: on" >>
/etc/elasticsearch/elasticsearch.yml  


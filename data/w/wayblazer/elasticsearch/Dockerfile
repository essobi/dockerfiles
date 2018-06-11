FROM elasticsearch:1.7.2  
# Install HEAD plugin  
RUN plugin --install mobz/elasticsearch-head  
  
#Install supervisor  
RUN apt-get update && apt-get install -y supervisor  
  
#Following config directory setup in the parent image.  
ADD config/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
#Data volume is defined as /usr/share/elasticsearch/data in parent.  
# Parent image exposes 9200, 9300  
CMD ["/run.sh"]  


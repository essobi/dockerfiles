FROM danielguerra/alpine-elasticsearch  
MAINTAINER Daniel Guerra <daniel.guerra69@gmail.com>  
  
USER root  
RUN /usr/share/java/elasticsearch/bin/elasticsearch-plugin install x-pack
--batch  
ADD elasticsearch.yml /usr/share/java/elasticsearch/config/elasticsearch.yml  
VOLUME
["/usr/share/java/elasticsearch/plugins","/usr/share/java/elasticsearch/config","/usr/share/java/elasticsearch/data","/dump"]  
EXPOSE 9200 9300  
ENTRYPOINT ["docker-entrypoint.sh"]  
USER elastico  
CMD ["/usr/share/java/elasticsearch/bin/elasticsearch"]  


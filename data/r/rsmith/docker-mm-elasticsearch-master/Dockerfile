FROM elasticsearch:1.7  
ADD config/elasticsearch.yml /usr/share/elasticsearch/config/  
ADD config/run.sh /usr/bin/  
  
RUN chmod +x /usr/bin/run.sh  
  
#Install plugins  
RUN /usr/share/elasticsearch/bin/plugin -install lmenezes/elasticsearch-
kopf/1.0  
RUN /usr/share/elasticsearch/bin/plugin -install elasticsearch/elasticsearch-
cloud-aws/2.7.1  
RUN /usr/share/elasticsearch/bin/plugin -install lukas-vlcek/bigdesk  
  
CMD ["/usr/bin/run.sh"]


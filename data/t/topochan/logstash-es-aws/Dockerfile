FROM logstash  
  
MAINTAINER Miguel Angel Guillen  
  
RUN plugin install logstash-output-amazon_es  
RUN apt-get update && apt-get -y install gettext-base && apt-get clean  
COPY logstash.conf /config-dir/logstash.tpl.conf  
COPY launcher.sh /config-dir/  
  
EXPOSE 5000/udp  
  
CMD ["/config-dir/launcher.sh"]  


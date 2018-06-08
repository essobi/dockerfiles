FROM elasticsearch:5  
MAINTAINER mishra.akshay91@gmail.com  
  
####### TAKE BACKUP OF DEFAULT ES CONFIG FILE #######  
  
RUN mv /usr/share/elasticsearch/config/elasticsearch.yml
"/usr/share/elasticsearch/config/elasticsearch.yml.bkp.$(date +"%Y-%m-%d")"  
  
####### ADD ES CUSTOM CONFIG FILE TO THE CONTAINER FS #########  
ADD ./config/elasticsearch.yml
/usr/share/elasticsearch/config/elasticsearch.yml  
  
ENV ES_JAVA_OPTS="-Des.path.conf=/etc/elasticsearch"  
  
CMD ["-E", "network.host=0.0.0.0", "-E",
"discovery.zen.minimum_master_nodes=1"]  


FROM fumihiro/dld-bootstrap  
  
MAINTAINER Fumihiro Kato <fumi@fumi.me>  
  
RUN apt-get update && apt-get install -y wget  
  
COPY docker/run.sh docker/dbpedia-dld.yml /download.sh /  
  
RUN chmod +x /run.sh  
  
VOLUME ["/dld-dbpedia-wd/models/"]  
  
ENTRYPOINT ["/run.sh"]  


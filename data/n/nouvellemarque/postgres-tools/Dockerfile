FROM postgres  
MAINTAINER Erik Allais <e.allais@nouvellemarque.com>  
  
RUN groupadd -r -g 1000 user1000 && useradd -r -g user1000 -u 1000 user1000  
  
VOLUME ["/data"]  
  
COPY postgres.sh /usr/local/bin/  
  
COPY docker-entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  


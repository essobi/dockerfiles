FROM postgres  
  
ADD install.sql /install.sql  
USER postgres  
USER root  
  
VOLUME /var/lib/postgresql/data  
ADD entrypoint /entrypoint  
ENTRYPOINT ["/bin/bash", "-c", "/entrypoint", "/docker-entrypoint.sh"]


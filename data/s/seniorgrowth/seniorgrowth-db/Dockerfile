FROM postgres:9.5  
RUN apt-get update  
  
RUN apt-get autoremove -y && apt-get install -y --no-install-recommends curl
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /docker-entrypoint-initdb.d  
COPY docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/  
COPY SGDB-10-05-15.tar /  


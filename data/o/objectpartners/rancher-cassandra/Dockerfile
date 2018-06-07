FROM cassandra:2.2.3  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  


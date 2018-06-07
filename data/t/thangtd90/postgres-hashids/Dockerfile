FROM postgres:9.6  
COPY pg_hashids /tmp/pg_hashids  
  
RUN apt-get update && apt-get install -y apt-utils make gcc postgresql-server-
dev-9.6  
  
RUN cd /tmp/pg_hashids/ && make; make install  
  
RUN rm -rf /tmp/pg_hashids  
  


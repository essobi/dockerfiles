FROM postgres:10-alpine  
  
ENV POSTGRES_USER postgres  
ENV POSTGRES_PASSWORD 1234  
ENV POSTGRES_DB sda-contest  
  
  
ADD 000_init.sql /docker-entrypoint-initdb.d/  
ADD 001_dummy_contest.sql /docker-entrypoint-initdb.d/  


FROM postgres:9-alpine  
  
MAINTAINER flo "florinutz@gmail.com"  
ARG importUser  
ARG importDb  
  
ENV importUser=$importUser  
ENV importDb=$importDb  
  
ADD dump.tar /  
  
RUN pg_restore -U $POSTGRES_USER -d $POSTGRES_DB /dump.tar -v  


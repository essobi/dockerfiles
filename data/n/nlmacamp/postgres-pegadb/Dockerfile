#FROM nlmacamp/pljava  
FROM nlmacamp/postgres-pljava  
  
RUN \  
locale-gen nl_NL && \  
locale-gen nl_NL.UTF-8 && \  
locale -a  
  
ADD init/*.sql /docker-entrypoint-initdb.d/  


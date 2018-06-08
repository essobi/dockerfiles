FROM mysql:5.5  
RUN apt-get update && apt-get install -y curl --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
ADD updatedb.sh /docker-entrypoint-initdb.d/updatedb.sh  
  
ENV MYSQL_DATABASE coa  
ENV MYSQL_USER coa  
ENV MYSQL_PASSWORD coa  
ENV MYSQL_ROOT_PASSWORD coa  
  
CMD ["mysqld", "--lower_case_table_names=1", "--character-set-server=utf8", "
--collation-server=utf8_unicode_ci"]


FROM mysql  
MAINTAINER Talles Bertann "talles.bertann@gmail.com"  
ADD assets/01_create_repository_mysql.sql /docker-entrypoint-
initdb.d/01_create_repository_mysql.sql  
ADD assets/02_create_quartz_mysql.sql /docker-entrypoint-
initdb.d/02_create_quartz_mysql.sql  
ADD assets/03_create_jcr_mysql.sql /docker-entrypoint-
initdb.d/03_create_jcr_mysql.sql


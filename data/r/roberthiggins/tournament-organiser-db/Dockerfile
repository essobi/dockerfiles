# DB  
  
FROM postgres:9.3  
MAINTAINER Robert Higgins <robert.h.higgins@gmail.com>  
  
ADD setup/ /docker-entrypoint-initdb.d/  
ADD data/ /docker-entrypoint-initdb.d/data/  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  


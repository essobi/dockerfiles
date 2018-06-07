FROM postgres:9.4  
MAINTAINER Frank Förster <frank.foerster@biozentrum.uni-wuerzburg.de>  
  
ADD 000_fix-acl.sh /docker-entrypoint-initdb.d/  
ADD 010_create_user_db.sh /docker-entrypoint-initdb.d/  


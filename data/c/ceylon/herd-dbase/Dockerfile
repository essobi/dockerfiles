#  
# Image for running the PostgreSQL database needed for Ceylon Herd  
#  
FROM postgres  
  
MAINTAINER Tako Schotanus <tako@ceylon-lang.org>  
  
LABEL org.ceylon-lang.dockerfile.description="Image for running the PostgreSQL
database needed for Ceylon Herd" \  
org.ceylon-lang.dockerfile.vendor="RedHat" \  
org.ceylon-lang.dockerfile.version="1.0"  
  
ENV POSTGRES_DB=ceylon-herd  
  
ADD docker-entrypoint-initdb.d /docker-entrypoint-initdb.d  
ADD add-herd-user.sh add-herd-user.sh  
ADD add-herd-admin.sh add-herd-admin.sh  


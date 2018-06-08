FROM efrecon/mini-tcl:latest  
MAINTAINER Emmanuel Frecon <efrecon@gmail.com>  
  
RUN apk add --update-cache mariadb-client-libs postgresql-client && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["tclsh8.6"]  


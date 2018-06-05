#vim:set ft=dockerfile:  
FROM postgres:latest  
  
MAINTAINER Jochen Faehnlein <jochen.faehnlein@ff-ipsheim.de>  
  
# push the SQL init scripts to image  
#RUN mkdir /docker-entrypoint-initdb.d  
ADD docker-entrypoint-initdb.d/init-db.sql /docker-entrypoint-initdb.d/  
  
# make the "de_DE.UTF-8" locale so postgres will be utf-8 enabled by default  
RUN localedef -i de_DE -c -f UTF-8 -A /usr/share/locale/locale.alias
de_DE.UTF-8  
ENV LANG de_DE.utf8  
  


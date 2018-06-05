FROM ubuntu:xenial  
RUN groupadd -g 999 mysql && useradd --uid 999 --gid 999 mysql  
RUN mkdir -p /volumes/wpprod && mkdir /volumes/wpstage && mkdir /volumes/wpdev
&& mkdir /volumes/dbprod && \  
mkdir /volumes/dbstage && mkdir /volumes/dbdev && mkdir /volumes/dbexport &&
mkdir /volumes/backups  
RUN apt-get update && apt-get upgrade -y && apt-get install -y rsync && apt-
get clean  
COPY bin/* /usr/local/bin/  
RUN chmod +x /usr/local/bin/*  
  
RUN chown -R www-data:www-data /volumes/wp*  
RUN chown -R mysql:mysql /volumes/db*  
  
CMD while true; do /usr/local/bin/fix_permissions.sh; sleep 60m; done  


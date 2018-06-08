FROM postgres:9.3.10  
MAINTAINER Jakob Runge <runjak@gmail.com>  
  
LABEL lingdb="postgres_backup" \  
version="1.1.2" \  
documentation="https://github.com/lingdb/container/wiki/postgres#the-
postgresbackup-container"  
  
COPY backup.sh /  
  
RUN apt-get update \  
&& apt-get install -y bzip2 \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /backup \  
&& chmod u+x /backup.sh  
  
ENTRYPOINT /backup.sh  


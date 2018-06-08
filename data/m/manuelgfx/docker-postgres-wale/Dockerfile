FROM postgres:9.4.5  
MAINTAINER Manuel Familia  
  
RUN apt-get update && apt-get install -y python-pip python-dev lzop pv
daemontools  
RUN easy_install wal-e  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME "/etc/wal-e/env"  
  
COPY scripts/docker-entrypoint.sh /docker-entrypoint.sh  
  
ADD scripts/fix-acl.sh /docker-entrypoint-initdb.d/  
ADD scripts/setup-wale.sh /docker-entrypoint-initdb.d/  


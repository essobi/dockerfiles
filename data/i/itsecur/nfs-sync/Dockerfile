FROM debian:jessie  
MAINTAINER Philipp Holler <philipp.holler93@googlemail.com>  
  
RUN apt-get update \  
&& apt-get install -y nfs-common netbase rsync \  
&& rm -r /var/lib/apt/lists/*  
  
ADD nfs-sync_entrypoint.sh /  
RUN chmod +x /nfs-sync_entrypoint.sh  
ENTRYPOINT ["/nfs-sync_entrypoint.sh"]


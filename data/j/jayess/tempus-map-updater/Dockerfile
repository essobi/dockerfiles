FROM debian:jessie  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -qy install --no-
install-recommends wget ca-certificates bzip2  
  
COPY ./map_updater.sh /usr/local/bin/map_updater.sh  
COPY ./default_level_sounds.txt /srv/default_level_sounds.txt  
  
ENTRYPOINT ["/usr/local/bin/map_updater.sh"]  


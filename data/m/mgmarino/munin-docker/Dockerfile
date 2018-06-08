FROM jekil/docker-munin-server:latest  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libwww-perl \  
libjson-perl  
  
COPY run.sh /usr/local/bin/start-munin-node  
COPY couchdb /usr/share/munin/plugins/couchdb  
COPY munin.conf /etc/munin/munin.conf  
COPY munin-node.conf /etc/munin/munin-node.conf  
COPY get_all_dbs.py /get_all_dbs.py  
  
CMD ["start-munin-node"]  


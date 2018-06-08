FROM debian:jessie  
  
RUN apt-get clean && \  
echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get -y -t jessie-backports install sphinxsearch cron && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY crontab /etc/  
  
CMD indexer --all --rotate || true && \  
cron && \  
searchd -c /etc/sphinxsearch/sphinx.conf --nodetach  


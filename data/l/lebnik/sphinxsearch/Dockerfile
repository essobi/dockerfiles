FROM debian:jessie  
  
MAINTAINER Lebedenko Nikolay <lebnikpro@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
libexpat1 \  
libmysqlclient18 \  
libodbc1 \  
libpq5  
ADD
http://sphinxsearch.com/files/sphinxsearch_2.2.10-release-1~jessie_amd64.deb
./  
RUN dpkg -i sphinxsearch_2.2.10-release-1~jessie_amd64.deb  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD indexer --all && searchd -c /etc/sphinxsearch/sphinx.conf --nodetach


FROM debian:wheezy  
MAINTAINER nise_nabe <nise.nabe@gmail.com>  
  
RUN apt-get update && apt-get --yes upgrade  
RUN apt-get install --yes curl  
RUN apt-get install --yes libexpat1 libmysqlclient18 libpq5 mysql-common  
  
RUN cd /tmp && curl -O
http://sphinxsearch.com/files/sphinxsearch_2.1.4-release-1~wheezy_amd64.deb  
RUN dpkg -i /tmp/sphinxsearch_2.1.4-release-1~wheezy_amd64.deb  


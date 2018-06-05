FROM bezrukovp/main-base  
MAINTAINER Pavel Bezrukov "bezrukov.ps@gmail.com"  
# Install sphinx search  
RUN apt-get -y -q install mysql-client-5.6 unixodbc libpq5  
RUN wget
http://sphinxsearch.com/files/sphinxsearch_2.2.9-release-0ubuntu12~trusty_amd64.deb  
RUN dpkg -i sphinxsearch_2.2.9-release-0ubuntu12~trusty_amd64.deb  
RUN rm -r -f sphinxsearch_2.2.9-release-0ubuntu12~trusty_amd64.deb  
RUN mv /etc/sphinxsearch/sphinx.conf /etc/sphinxsearch/sphinx.conf.bak  
ADD etc/sphinxsearch/dicts /etc/sphinxsearch/dicts  
ADD etc/sphinxsearch/sphinx.conf /etc/sphinxsearch/sphinx.conf  
  
# Sphinx Plain Port  
EXPOSE 9312  
# SphinxQL Port  
EXPOSE 9306


FROM debian:jessie  
  
RUN apt-get update && apt-get install -y --no-install-recommends wget
libexpat1 libmysqlclient18 libodbc1 libpq5  
  
RUN cd /tmp && \  
wget
"http://sphinxsearch.com/files/sphinxsearch_2.2.11-release-1~jessie_amd64.deb"
&& \  
dpkg -i "sphinxsearch_2.2.11-release-1~jessie_amd64.deb"  
  
RUN apt-get autoremove -y && apt-get clean all && rm -R /tmp  
  
COPY sphinx.conf /etc/sphinxsearch/sphinx.conf  
  
ADD start.sh /  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  


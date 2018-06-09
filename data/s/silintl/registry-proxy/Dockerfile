FROM silintl/apache2  
MAINTAINER "Peter Kohler" <peter_kohler@sil.org>  
  
RUN apt-get update && apt-get install -y \  
s3cmd  
  
# Turn on apache2 modules  
RUN a2enmod proxy_http \  
&& a2enmod ssl  
  
COPY expand.sh /  
COPY rproxy_site.conf $HTTPD_PREFIX/sites-available/rproxy_site.conf  
COPY ssl.conf $HTTPD_PREFIX/mods-available/ssl.conf  
  
COPY start_apache2.sh /  
  
RUN a2ensite rproxy_site  
  
EXPOSE 443  
ENTRYPOINT ["/expand.sh"]  
CMD ["/start_apache2.sh"]  


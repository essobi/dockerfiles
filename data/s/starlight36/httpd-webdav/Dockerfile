FROM httpd  
  
RUN apt-get update && apt-get install -y --no-install-recommends
libaprutil1-ldap  
  
RUN sed -i 's|#LoadModule dav_module|LoadModule dav_module|g'
/usr/local/apache2/conf/httpd.conf && \  
sed -i 's|#LoadModule dav_fs_module|LoadModule dav_fs_module|g'
/usr/local/apache2/conf/httpd.conf && \  
sed -i 's|#Include conf/extra/httpd-dav.conf|Include conf/extra/httpd-
dav.conf|g' /usr/local/apache2/conf/httpd.conf  
  
RUN cp -r /usr/local/apache2/conf /tmp/httpd-conf  
  
COPY entrypoint.sh /usr/local/sbin/entrypoint.sh  
RUN chmod +x /usr/local/sbin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]  
EXPOSE 80  
CMD ["httpd-foreground"]


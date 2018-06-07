FROM httpd:2.4  
LABEL maintainer="EEA: IDM2 A-Team <eea-edw-a-team-alerts@googlegroups.com>"  
  
RUN runDeps="curl less libaprutil1-ldap openssl ca-certificates" \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends $runDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i 's|User daemon|User www-data|' /usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|Group daemon|Group www-data|' /usr/local/apache2/conf/httpd.conf
\  
&& sed -i 's|#LoadModule rewrite_module|LoadModule rewrite_module|'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule proxy_module|LoadModule proxy_module|'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule proxy_http_module|LoadModule proxy_http_module|'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule deflate_module modules/mod_deflate.so|LoadModule
deflate_module modules/mod_deflate.so|' /usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#Include conf/extra/httpd-autoindex.conf|Include
conf/extra/httpd-autoindex.conf|' /usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule ldap_module|LoadModule ldap_module|'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule authnz_ldap_module|LoadModule authnz_ldap_module|'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule session_module|LoadModule session_module|'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule session_cookie_module|LoadModule
session_cookie_module|' /usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule session_dbd_module|LoadModule session_dbd_module|'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule auth_form_module|LoadModule auth_form_module|'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule request_module|LoadModule request_module|'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule ssl_module|LoadModule ssl_module|'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#LoadModule socache_shmcb_module|LoadModule
socache_shmcb_module|' /usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#Include conf/extra/httpd-ssl.conf|Include conf/extra/httpd-
ssl.conf|' /usr/local/apache2/conf/httpd.conf \  
&& sed -i 's|#ServerName www.example.com:80|ServerName eeacms-
apache.docker.com|' /usr/local/apache2/conf/httpd.conf \  
&& echo 'IncludeOptional conf/extra/vh-*.conf' >>
/usr/local/apache2/conf/httpd.conf  
  
COPY docker-entrypoint.sh /  
COPY reload.sh /bin/reload  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["httpd-foreground"]  


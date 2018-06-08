FROM httpd:2.4  
MAINTAINER Alterway <iac@alterway.fr>  
  
# libaprutil1-ldap runtime dependency to use the LDAP  
#RUN apt-get update \  
# && apt-get install -y --no-install-recommends libaprutil1-ldap \  
# && rm -r /var/lib/apt/lists/*  
RUN useradd -ms /bin/bash http  
  
ENV LOCALTIME Europe/Paris  
ENV HTTPD_CONF_DIR $HTTPD_PREFIX/conf/conf-enabled/  
ENV HTTPD__DocumentRoot /var/www/html  
ENV HTTPD_Directory_AllowOverride All  
ENV HTTPD_Directory_Options 'Indexes FollowSymLinks'  
ENV HTTPD__User http  
ENV HTTPD__Group http  
  
  
RUN mkdir -p $HTTPD_CONF_DIR && \  
sed -i "s/DocumentRoot.*/DocumentRoot \${HTTPD__DocumentRoot}/"
$HTTPD_PREFIX/conf/httpd.conf && \  
sed -i "s/\/usr\/local\/apache2\/htdocs/\${HTTPD__DocumentRoot}/"
$HTTPD_PREFIX/conf/httpd.conf && \  
sed -i "s/AllowOverride None/AllowOverride \${HTTPD_Directory_AllowOverride}/"
$HTTPD_PREFIX/conf/httpd.conf && \  
sed -i "s/Options Indexes FollowSymLinks/Options \${HTTPD_Directory_Options}/"
$HTTPD_PREFIX/conf/httpd.conf && \  
echo 'IncludeOptional conf/conf-enabled/*.conf' >>
$HTTPD_PREFIX/conf/httpd.conf && \  
echo 'ServerName ${HOSTNAME}' > $HTTPD_CONF_DIR/00-default.conf  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
WORKDIR /var/www  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  


FROM secoresearch/varnish  
  
# INSTALL  
RUN apt-get update  
RUN apt-get install -y apache2  
RUN apt-get install -y php  
RUN apt-get install -y php-xml  
RUN apt-get install -y php-mbstring  
RUN apt-get install -y php-curl  
RUN apt-get install -y php-zip  
# envsubst from gettext-base can be used to replace environment variables in
config files etc.  
RUN apt-get install -y gettext-base  
  
RUN a2dismod ssl  
RUN a2enmod rewrite  
RUN a2enmod cgi  
  
# ENVIRONMENT VARIABLES  
ENV PATH_VAR_APACHE "/var/run/apache2"  
ENV APACHE_LOG_DIR "/var/log/apache2"  
ENV FILE_LOG_APACHE_ERROR "$APACHE_LOG_DIR/error.log"  
ENV FILE_LOG_APACHE_ACCESS "$APACHE_LOG_DIR/access.log"  
ENV FILE_CONF_PORTS "/etc/apache2/ports.conf"  
ENV FILE_CONF_VHOST "/etc/apache2/sites-available/000-default.conf"  
ENV PATH_HTML "/var/www/html"  
ENV APACHE_OPTIONS "Indexes FollowSymlinks"  
ENV APACHE_ALLOW_OVERRIDE "None"  
ENV FILE_GENERATE_CONF_VHOST_SH "/generate-conf-vhost.sh"  
COPY ports.conf "$FILE_CONF_PORTS"  
COPY generate-conf-vhost.sh "$FILE_GENERATE_CONF_VHOST_SH"  
  
# PERMISSIONS  
RUN mkdir -p "$PATH_VAR_APACHE"  
RUN mkdir -p "$APACHE_LOG_DIR"  
RUN chgrp -R root "$APACHE_LOG_DIR"  
RUN chmod -R g=u "$APACHE_LOG_DIR"  
RUN chmod -R g=u "$PATH_VAR_APACHE"  
RUN touch "$FILE_CONF_PORTS"; chgrp root "$FILE_CONF_PORTS"; chmod -R g+rw
"$FILE_CONF_PORTS"  
RUN rm "$FILE_CONF_VHOST"; touch "$FILE_CONF_VHOST"; chgrp root
"$FILE_CONF_VHOST"; chmod -R g+rw "$FILE_CONF_VHOST"  
RUN mkdir -p "$PATH_HTML"; chgrp root "$PATH_HTML"; chmod -R g=u "$PATH_HTML"  
  
ENV RUN_APACHE_VARNISH /run-apache-varnish.sh  
ENV EXEC_APACHE_VARNISH "exec $RUN_APACHE_VARNISH"  
COPY run "$RUN_APACHE_VARNISH"  
  
ENTRYPOINT [ "/run-apache-varnish.sh" ]  


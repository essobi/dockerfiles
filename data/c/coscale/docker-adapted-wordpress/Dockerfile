FROM wordpress:4.7-apache  
  
RUN sed -i -e "s/Custom.*/LogFormat \"%V \\\\\\\\\"%r\\\\\\\\\" %D %s %I %O\"
coscale\n\tCustomLog \${APACHE_LOG_DIR}\/access.log coscale/g"
/etc/apache2/sites-available/000-default.conf \  
&& sed -i -e "s/Require local//g" /etc/apache2/mods-available/status.conf \  
&& sed -i -e "s/#Require .*/Require local/g" /etc/apache2/mods-
available/status.conf \  
&& sed -i -e "s/RewriteCond %{REQUEST_FILENAME} \\!-d/RewriteCond
%{REQUEST_FILENAME} \\!-d\nRewriteCond %{REQUEST_URI} !=\/server-status/g"
/usr/local/bin/docker-entrypoint.sh  
  
LABEL
com.coscale.monitoring='[{"PluginType":"APACHE","Configuration":{"FILE":["\"/dev/stdout\"
\"%V \"%r\" %D %s %I %O\""],"STATS URL":["http://localhost/server-
status"],"URL CHECK":["http://localhost"]}}]'  


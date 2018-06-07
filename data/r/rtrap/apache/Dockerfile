FROM rtrap/debian:latest  
  
# install apache simply from repository  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apache2 \  
&& rm -r /var/lib/apt/lists/*  
  
# setup http2 apache config  
RUN { \  
echo '<IfModule http2_module>'; \  
echo ' Protocols h2 h2c http/1.1'; \  
echo ' H2Direct on'; \  
echo '</IfModule>'; \  
} > /etc/apache2/mods-available/http2.conf  
RUN a2enmod http2  
  
# setup ssl apache config  
RUN sed -i "s|SSLCipherSuite HIGH\:\!aNULL|SSLCipherSuite
HIGH\:\!aNULL\:\!MD5|g" /etc/apache2/mods-available/ssl.conf \  
&& sed -i "s|SSLProtocol all \-SSLv3|SSLProtocol \-all \+TLSv1\.1
\+TLSv1\.2|g" /etc/apache2/mods-available/ssl.conf \  
&& sed -i "/<\/IfModule>/i #SSL certificates\n\  
BrowserMatch \"MSIE \[2\-6\]\" nokeepalive ssl\-unclean\-shutdown
downgrade-1\.0 force-response\-1\.0\n\  
BrowserMatch \"MSIE \[17\-9\]\" ssl\-unclean\-shutdown\n\  
Header always set Strict-Transport-Security \"max\-age\=31536000\;
includeSubDomains\; preload\"\n"\  
/etc/apache2/mods-available/ssl.conf \  
&& a2enmod ssl  
  
# setup directory for certificates  
RUN mkdir -p /etc/apache2/ssl  
  
# setup sites config to remove default 80 site  
RUN a2dissite 000-default \  
&& sed -i '/Listen 80/s/^/#/' /etc/apache2/ports.conf  
  
VOLUME ["/etc/apache2/ssl", "/etc/apache2/sites-
enabled","/var/www/html","/var/log/apache2"]  
  
EXPOSE 443  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  


FROM iitgdocker/aide:latest  
  
MAINTAINER "The Ignorant IT Guy" <iitg@gmail.com>  
  
# Make placeholder directories for the end user to mount against  
RUN mkdir -p /data/conf.d  
  
RUN yum -y --nogpgcheck install \  
httpd \  
mod_ssl \  
mod_security && \  
yum clean all  
  
RUN sed -i -e 's/<Directory "\/var\/www\/html">/<Directory
"\/var\/www\/html">\n<LimitExcept GET POST HEAD>\ndeny from
all\n<\/LimitExcept>/1' \  
-e 's/Options Indexes.*/Options -Indexes -Includes +FollowSymLinks/g' /etc/httpd/conf/httpd.conf  
  
# Allow overrides. Surely, there's gotta be a better way to do this...  
RUN awk '/ AllowOverride None/{count++;if(count==2){sub(" AllowOverride
None"," AllowOverride All")}}1' /etc/httpd/conf/httpd.conf
>/etc/httpd/conf/httpd.conf.new  
RUN mv /etc/httpd/conf/httpd.conf.new /etc/httpd/conf/httpd.conf  
  
# Secure Apache server as much as we can  
COPY secure.conf /etc/httpd/conf.d/secure.conf  
  
# Disable unused modules. It would be nice to disable more but  
# it may make this container less portable.  
# source: http://www.thegeekstuff.com/2011/03/apache-hardening/  
RUN sed -i \  
-e 's/LoadModule info_module/#LoadModule info_module/g' \  
-e 's/LoadModule userdir_module/#LoadModule userdir_module/g' \  
-e 's/LoadModule status_module/#LoadModule status_module/g' \  
-e 's/LoadModule env_module/#LoadModule env_module/g' \  
-e 's/LoadModule alias_module/#LoadModule alias_module/g' \  
-e 's/LoadModule include_module/#LoadModule include_module/g' \  
-e 's/LoadModule version_module/#LoadModule version_module/g' \  
/etc/httpd/conf.modules.d/00-base.conf  
  
# These files are also unnecessary  
RUN rm -vf /etc/httpd/conf.modules.d/00-systemd.conf
/etc/httpd/conf.d/autoindex.conf /etc/httpd/conf.d/welcome.conf  
  
# Configure SSL  
RUN sed -i -e 's/SSLProtocol.*/SSLProtocol all -SSLv3 -TLSv1.1/g' \  
-e 's/^SSLCipherSuite.*/SSLCipherSuite ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256/g' \  
-e 's/#SSLHonorCipherOrder on/SSLHonorCipherOrder on\nHeader add Strict-Transport-Security "max-age=15768000"/g' \  
-e 's/Listen 443 https/Listen 443 https\nSSLCompression off\nSSLUseStapling on\nSSLStaplingResponderTimeout 5\nSSLStaplingReturnResponderErrors off\nSSLStaplingCache shmcb:\/var\/run\/ocsp\\(128000\\)\n/g' \  
/etc/httpd/conf.d/ssl.conf  
  
# Download the apache mod security rules. These ones are pulled straight from
the mod_security git repo  
RUN curl -L --insecure -o /tmp/mod_security.tar.gz
http://files.gtenterprises.net.au/mod_security.tar.gz  
  
# Include end user apache configuration files  
RUN echo -e '# Include custom apache configuration files\nIncludeOptional
/data/conf.d/*.conf' >/etc/httpd/conf.d/custom.conf  
  
# Make sure /var/www/html knows who's boss.  
RUN chown -R apache:apache /var/www/html  
  
EXPOSE 80  
EXPOSE 443  
COPY apache.sh /apache.sh  
RUN chmod +x /apache.sh  
CMD ["/apache.sh"]  


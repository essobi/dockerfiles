FROM feduxorg/centos:latest  
MAINTAINER dev@fedux.org  
  
# ENV http_proxy http://172.17.42.1:3128  
# ENV https_proxy https://172.17.42.1:3128  
# Install and activate apache  
RUN groupadd -r -g 990 apache \  
&& useradd -r -u 990 -g apache apache \  
&& yum install -y httpd mod_ssl\  
&& systemctl enable httpd \  
&& yum clean -y all  
  
# Setting up configuration  
RUN rm -r /etc/httpd/conf.d/* \  
# Add Listener  
&& sed -ri -e '/Listen 80/ a \Listen 443' /etc/httpd/conf/httpd.conf \  
# Modify DocumentRoot  
&& sed -ri -e 's#/var/www/html#/srv/http#' /etc/httpd/conf/httpd.conf \  
&& sed -ri -e 's#/var/www#/srv/http#' /etc/httpd/conf/httpd.conf \  
# Logs  
&& sed -ri -e 's#logs/error_log#/var/log/httpd/error_log#'
/etc/httpd/conf/httpd.conf \  
&& sed -ri -e 's#logs/access_log#/var/log/httpd/access_log#'
/etc/httpd/conf/httpd.conf \  
# Activate Event Worker  
&& sed -ri -e '/mpm_prefork_module/s/LoadModule/#LoadModule/'
/etc/httpd/conf.modules.d/00-mpm.conf \  
&& sed -ri -e '/mpm_event_module/s/#LoadModule/LoadModule/'
/etc/httpd/conf.modules.d/00-mpm.conf \  
# Add section to load enabled sites  
&& sed -ri -e '$aIncludeOptional sites-enabled/*.conf'
/etc/httpd/conf/httpd.conf  
  
# Add SSL/TLS configuration  
ADD ssl.conf /etc/httpd/conf.d/ssl.conf  
  
# Download configuration  
RUN cd /tmp \  
&& curl -L https://github.com/h5bp/server-configs-apache/archive/master.tar.gz
| tar -xzf - -C .\  
&& mv server-configs-apache-master/dist/.htaccess /etc/httpd/conf.d/h5bp.conf
\  
&& rm -r server-configs-apache-master/  
  
# Activate Production Mode  
RUN sed -ri -e 's/#ServerTokens/ServerTokens/' /etc/httpd/conf.d/h5bp.conf  
  
# Setting up paths  
RUN install -d /srv/http \  
# Create Directory where the enabled sites should be installed  
&& install -d /etc/httpd/sites-enabled \  
# Create ssl directory  
&& install -d -g apache -m 0750 /etc/ssl/apache  
  
VOLUME ["/etc/httpd/sites-enabled", "/etc/ssl/httpd", "/var/log/httpd"]  
  
# Expose ports  
EXPOSE 80 443  
# Working Directory  
WORKDIR /  


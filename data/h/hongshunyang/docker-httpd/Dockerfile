FROM hongshunyang/docker-alpine  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
RUN apk add -U apache2 apache2-proxy  
  
COPY tmpl/_etc_apache2_httpd.conf.tmpl /etc/apache2/httpd.conf.tmpl  
## {{ default .Env.WEBROOT "/var/www/html" }}  
COPY rootfs/_usr_bin_httpd-foreground /usr/bin/httpd-foreground  
  
RUN chmod a+x /usr/bin/httpd-foreground \  
&& mkdir -p /run/apache2 \  
&& mkdir -p /var/www/html  
  
#VOLUME /var/www/html  
#TODO log  
EXPOSE 80 443  
CMD ["dockerize", "-template",
"/etc/apache2/httpd.conf.tmpl:/etc/apache2/httpd.conf", "httpd-foreground"]  
  


FROM tianon/centos:6.5  
MAINTAINER Ke Zhu <davidzhu.4.2@gmail.com>  
  
RUN yum -y install httpd mod_ssl  
RUN rm -f /etc/httpd/conf.d/ssl.conf  
  
ADD ./mod_ssl.conf /etc/httpd/conf.d/  
  
# env variables can be changed by docker  
ENV HTTPD_SSL_CIPHER_SUITE ALL:!ADH:!EXPORT:!SSLv2:RC4+RSA:+HIGH:+MEDIUM:+LOW  
  
EXPOSE 80 443  
VOLUME ["/var/www/html"]  
  
ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]


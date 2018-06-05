FROM centos:centos7  
MAINTAINER John Paul Alcala, jpalcala@ayannah.com  
  
RUN yum -y install epel-release && \  
yum -y upgrade && \  
yum -y install tar supervisor nginx php-fpm php-mysql php-mcrypt php-gd && \  
yum -y clean all && \  
rm -rf /var/cache/yum/* /tmp/*  
  
RUN groupadd -g 1000 www && \  
useradd -g www -u 1000 -r -M www && \  
mkdir -p /var/www/dokuwiki /var/lib/php/session && \  
curl http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz | tar xzf -
-C /var/www/dokuwiki --strip-components=1 && \  
chown -R www:www /var/www /var/lib/php/session  
  
COPY etc/ /etc/  
COPY dokuwiki-entrypoint.sh /  
  
RUN nginx -t  
  
EXPOSE 80  
VOLUME [ \  
"/var/www/dokuwiki/data/pages", \  
"/var/www/dokuwiki/data/meta", \  
"/var/www/dokuwiki/data/media", \  
"/var/www/dokuwiki/data/media_attic", \  
"/var/www/dokuwiki/data/media_meta", \  
"/var/www/dokuwiki/data/attic", \  
"/var/www/dokuwiki/conf", \  
"/var/www/dokuwiki/lib/plugins", \  
"/var/log" \  
]  
  
ENTRYPOINT ["/dokuwiki-entrypoint.sh"]  
CMD ["dokuwiki"]  


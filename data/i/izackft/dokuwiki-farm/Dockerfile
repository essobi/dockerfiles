FROM centos:7  
MAINTAINER Izack Franklin <izackft@gmail.com>  
  
ENV DOKUWIKI_VERSION 2017-02-19a  
ENV MD5_CHECKSUM 9b9ad79421a1bdad9c133e859140f3f2  
  
RUN yum groupinstall "Development tools" -y && \  
yum install openssl apr-devel libxm12-devel -y  
  
ADD src /usr/local/src  
  
RUN groupadd -g 48 apache && \  
useradd -m -d /home/apache2 -s /bin/nologin -g 48 -u 48 apache2  
  
RUN cd /usr/local/src/db-5.3.28 && \  
./compila.sh && \  
cd /usr/local/src/apr-1.5.2 && \  
./compila.sh && \  
cd /usr/local/src/apr-util-1.5.4 && \  
./compila.sh && \  
cd /usr/local/src/pcre-8.38 && \  
./compila.sh && \  
cd /usr/local/src/httpd-2.4.18 && \  
./compila.sh && \  
cd /usr/local/src/php-5.4.16 && \  
./compila.sh && \  
rm -rf /usr/local/src/*  
  
RUN mkdir -p /var/www/dokuwiki /var/www/farm && \  
cd /var/www/dokuwiki && \  
curl -O -L
"https://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz" &&
\  
tar -xzf "dokuwiki-$DOKUWIKI_VERSION.tgz" \--strip 1 && \  
rm "dokuwiki-$DOKUWIKI_VERSION.tgz"  
  
ADD apache2/conf /usr/local/apache2/conf  
ADD apache2/modules /usr/local/apache2/modules  
ADD plugins/farmer /var/www/dokuwiki/lib/plugins/farmer  
ADD plugins/konsole /var/www/dokuwiki/lib/plugins/konsole  
ADD plugins/tools /var/www/dokuwiki/lib/plugins/tools  
ADD plugins/sidebar /var/www/dokuwiki/lib/plugins/sidebar  
ADD plugins/note /var/www/dokuwiki/lib/plugins/note  
ADD plugins/avatar /var/www/dokuwiki/lib/plugins/avatar  
ADD plugins/indexmenu /var/www/dokuwiki/lib/plugins/indexmenu  
ADD plugins/dw2pdf /var/www/dokuwiki/lib/plugins/dw2pdf  
  
ADD start.sh /start.sh  
  
RUN /bin/chmod +x /start.sh  
  
EXPOSE 80  
VOLUME ["/var/www/dokuwiki"]  
VOLUME ["/var/www/farm"]  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["/start.sh"]  


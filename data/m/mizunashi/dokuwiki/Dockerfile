FROM debian:jessie  
MAINTAINER Mizunashi Mana <mizunashi_mana@mma.club.uec.ac.jp>  
  
RUN apt-get update \  
&& apt-get -y install tar curl supervisor nginx  
  
# Installing HHVM  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 \  
&& echo deb http://dl.hhvm.com/debian jessie main | tee
/etc/apt/sources.list.d/hhvm.list  
RUN apt-get update && apt-get -y install hhvm \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY install.sh /usr/share/dokuwiki/  
RUN bash /usr/share/dokuwiki/install.sh  
  
# Installing Dockuwiki  
RUN mkdir -p /var/www/dokuwiki/ && cd /var/www/dokuwiki/ \  
&& curl http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz | tar xz
--strip 1 \  
&& chown -R www-data:www-data /var/www  
COPY dokuwiki-site /etc/nginx/sites-enabled/  
  
# Please, execute `docker exec wiki_container after_install` after dokuwiki
installed  
COPY after_install.sh /bin/after_install  
RUN chmod +x /bin/after_install  
  
EXPOSE 80  
VOLUME ["/var/www/dokuwiki/data/",
"/var/www/dokuwiki/lib/plugins","/var/www/dokuwiki/conf/","/var/www/dokuwiki/lib/tpl/"]  
  
CMD ["/usr/bin/supervisord", "-n"]  


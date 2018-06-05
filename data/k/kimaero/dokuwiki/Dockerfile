FROM alpine:latest  
MAINTAINER Denis Kim <denis@kim.aero>  
  
RUN apk update  
RUN apk upgrade  
RUN apk add libressl2.4-libssl libressl2.4-libcrypto \  
php7 php7-fpm php7-gd php7-openssl php7-session php7-xml php7-zlib \  
nginx supervisor curl tar \  
ca-certificates wget openssl  
RUN update-ca-certificates  
  
RUN mkdir -p /run/nginx && \  
mkdir -p /var/www && \  
cd /var/www && \  
curl -O -L "https://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz" &&
\  
tar -xzf "dokuwiki-stable.tgz" \--strip 1 && \  
rm "dokuwiki-stable.tgz"  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD supervisord.conf /etc/supervisord.conf  
ADD start.sh /start.sh  
  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php7/php-fpm.ini && \  
sed -i -e "s|;daemonize\s*=\s*yes|daemonize = no|g" /etc/php7/php-fpm.conf &&
\  
sed -i -e "s|listen\s*=\s*127\\.0\\.0\\.1:9000|listen = /var/run/php-
fpm7.sock|g" /etc/php7/php-fpm.d/www.conf && \  
sed -i -e "s|;listen\\.owner\s*=\s*|listen.owner = |g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s|;listen\\.group\s*=\s*|listen.group = |g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s|;listen\\.mode\s*=\s*|listen.mode = |g" /etc/php7/php-
fpm.d/www.conf && \  
chmod +x /start.sh  
  
RUN mkdir /var/www/lib/tpl/bootstrap3 && \  
wget -O- "https://github.com/LotarProject/dokuwiki-template-
bootstrap3/archive/master.tar.gz" | tar xz --strip 1 -C
/var/www/lib/tpl/bootstrap3  
RUN mkdir /var/www/lib/plugins/backup && \  
wget -O- "https://github.com/tatewake/dokuwiki-plugin-
backup/archive/master.tar.gz" | tar xz --strip 1 -C
/var/www/lib/plugins/backup  
RUN mkdir /var/www/lib/plugins/emoji && \  
wget -O- "https://github.com/ptbrown/dokuwiki-plugin-
emoji/archive/master.tar.gz" | tar xz --strip 1 -C /var/www/lib/plugins/emoji  
RUN mkdir /var/www/lib/plugins/wrap && \  
wget -O-
"https://github.com/selfthinker/dokuwiki_plugin_wrap/archive/stable.tar.gz" |
tar xz --strip 1 -C /var/www/lib/plugins/wrap  
RUN mkdir /var/www/lib/plugins/upgrade && \  
wget -O- "https://github.com/splitbrain/dokuwiki-plugin-
upgrade/archive/master.tar.gz" | tar xz --strip 1 -C
/var/www/lib/plugins/upgrade  
RUN mkdir /var/www/lib/plugins/tag && \  
wget -O- "https://github.com/dokufreaks/plugin-tag/archive/master.tar.gz" |
tar xz --strip 1 -C /var/www/lib/plugins/tag  
RUN mkdir /var/www/lib/plugins/pageredirect && \  
wget -O- "https://github.com/glensc/dokuwiki-plugin-
pageredirect/archive/master.tar.gz" | tar xz --strip 1 -C
/var/www/lib/plugins/pageredirect  
RUN mkdir /var/www/lib/plugins/note && \  
wget -O-
"https://github.com/MischaTheEvil/dokuwiki_note/archive/master.tar.gz" | tar
xz --strip 1 -C /var/www/lib/plugins/note  
RUN mkdir /var/www/lib/plugins/indexmenu && \  
wget -O- "https://github.com/samuelet/indexmenu/archive/master.tar.gz" | tar
xz --strip 1 -C /var/www/lib/plugins/indexmenu  
RUN mkdir /var/www/lib/plugins/move && \  
wget -O- "https://github.com/michitux/dokuwiki-plugin-
move/archive/master.tar.gz" | tar xz --strip 1 -C /var/www/lib/plugins/move  
RUN mkdir /var/www/lib/plugins/ckgedit && \  
wget -O- "https://github.com/turnermm/ckgedit/archive/master.tar.gz" | tar xz
--strip 1 -C /var/www/lib/plugins/ckgedit  
RUN mkdir /var/www/lib/plugins/csv && \  
wget -O- "https://github.com/cosmocode/csv/archive/master.tar.gz" | tar xz
--strip 1 -C /var/www/lib/plugins/csv  
RUN mkdir /var/www/lib/plugins/dw2pdf && \  
wget -O- "https://github.com/splitbrain/dokuwiki-plugin-
dw2pdf/archive/master.tar.gz" | tar xz --strip 1 -C
/var/www/lib/plugins/dw2pdf  
RUN mkdir /var/www/lib/plugins/include && \  
wget -O- "https://github.com/dokufreaks/plugin-include/archive/master.tar.gz"
| tar xz --strip 1 -C /var/www/lib/plugins/include  
RUN mkdir /var/www/lib/plugins/discussion && \  
wget -O- "https://github.com/dokufreaks/plugin-
discussion/archive/master.tar.gz" | tar xz --strip 1 -C
/var/www/lib/plugins/discussion  
RUN mkdir /var/www/lib/plugins/edittable && \  
wget -O- "https://github.com/cosmocode/edittable/archive/master.tar.gz" | tar
xz --strip 1 -C /var/www/lib/plugins/edittable  
RUN mkdir /var/www/lib/plugins/nspages && \  
wget -O- "https://github.com/gturri/nspages/archive/master.tar.gz" | tar xz
--strip 1 -C /var/www/lib/plugins/nspages  
RUN mkdir /var/www/lib/plugins/addnewpage && \  
wget -O- "https://github.com/samwilson/dokuwiki-plugin-
addnewpage/archive/master.tar.gz" | tar xz --strip 1 -C
/var/www/lib/plugins/addnewpage  
  
RUN chown -R nobody:nobody /var/www/lib/  
  
EXPOSE 80  
VOLUME ["/var/www/data", "/var/www/conf", "/var/www/lib/plugins/",
"/var/www/lib/tpl/"]  
CMD /start.sh  
  


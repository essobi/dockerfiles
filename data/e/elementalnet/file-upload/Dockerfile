FROM debian:jessie-slim AS build  
  
ENV JQUERY_FILE_UPLOAD_VERSION v9.19.1  
ADD https://github.com/blueimp/jQuery-File-
Upload/archive/${JQUERY_FILE_UPLOAD_VERSION}.tar.gz /jQuery-File-Upload.tar.gz  
RUN mkdir /jQuery-File-Upload && \  
tar --strip-components=1 -C /jQuery-File-Upload -xzf /jQuery-File-
Upload.tar.gz && \  
rm -rf /jQuery-File-Upload/*.html /jQuery-File-Upload/test/ /jQuery-File-
Upload/server/gae-go/ \  
/jQuery-File-Upload/server/gae-python/  
  
FROM debian:jessie-slim AS runtime  
  
COPY \--from=build /jQuery-File-Upload/ /var/www/upload/  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
RUN apt-get update && \  
apt-get upgrade -y -q && \  
apt-get -y -q --force-yes install --no-install-recommends \  
wget \  
apt-transport-https \  
ca-certificates  
  
RUN apt-get -y -q --force-yes install --no-install-recommends \  
openssh-server \  
supervisor \  
joe \  
less \  
# For jquery-file-upload  
imagemagick \  
php5-gd \  
php5-imagick \  
php5-apcu \  
libapache2-mod-php5 \  
apache2 \  
apache2-utils && \  
apt-get clean -y -q  
  
ADD supervisord.conf /supervisord.conf  
ADD jquery-file-upload/index.html /var/www/upload/index.html  
ADD php/php.ini /etc/php5/apache2/php.ini  
ADD apache/apache2.conf /etc/apache2/apache2.conf  
ADD apache/000-default.conf /etc/apache2/sites-available/000-default.conf  
ADD sshd_config /tmp/sshd_config  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN mkdir -p /var/run/sshd /var/www/upload/server/php/chroot && \  
mv /var/www/upload/server/php/files /var/www/upload/server/php/chroot && \  
mv /var/www/upload/server/php/chroot/files/.htaccess
/var/www/upload/server/php/chroot && \  
ln -s /var/www/upload/server/php/chroot/files /var/www/upload/server/php/files
&& \  
perl -i -pl -e 's/^#?(\s*PermitRootLogin\s+)[\w\\-]+$/$1no/i;' \  
-e 's/^#?(\s*PasswordAuthentication\s+)\w+$/$1no/i' /etc/ssh/sshd_config && \  
chmod a+x /docker-entrypoint.sh && \  
ln -s /etc/apache2/mods-available/headers.load /etc/apache2/mods-
enabled/headers.load && \  
ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load && \  
cat /tmp/sshd_config >>/etc/ssh/sshd_config && \  
chmod 775 /var/www/upload/server/php/chroot/files && \  
chmod 755 /var /var/www /var/www/upload /var/www/upload/server
/var/www/upload/server/php \  
/var/www/upload/server/php/chroot && \  
echo "Put your files into /files. Don't use subdirectories.\nThey cannot be
accessed via the web user interface!" \  
>/var/www/upload/server/php/chroot/README.txt && \  
rm -rf /var/lib/apt/lists/* /var/cache/* /tmp/* /var/tmp/*
/var/www/upload/server/php/chroot/files/.gitignore /tmp/sshd_config  
  
VOLUME [ "/var/www/upload/server/php/chroot/files" ]  
EXPOSE 22 80  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD ["/usr/bin/supervisord", "-c", "/supervisord.conf", "-u", "root", "-n"]  


FROM greyltc/archlinux  
MAINTAINER martin@gabelmann.biz  
  
ENV DB_TYPE=pgsql \  
DB_HOST=localhost \  
DB_NAME=owncloud_db \  
DB_USER=owncloud \  
DB_PREFIX="" \  
DB_PASS=changemepls \  
DB_EXTERNAL=false \  
OC_ADMIN=admin \  
OC_ADMINPASS=changemepls \  
OC_DATADIR=/srv/http/data \  
OC_EMAIL="admin@localhost" \  
OC_DOMAIN="localhost" \  
OC_BACKUP_CRON=no \  
OC_BACKUP_FILES=1 \  
OC_BACKUP_DIR=/backup \  
OC_TIME="Europe/Berlin" \  
OC_LC="en_US.UTF-8"  
RUN pacman -Syyu --noconfirm &&\  
pacman -S vim apache php php-apache php-mcrypt php-intl php-gd php-pgsql
postgresql php-apcu-bc fcron --noconfirm --needed &&\  
pacman -Sc --noconfirm  
  
RUN /usr/bin/install -g http -m 775 -d /run/httpd  
RUN /usr/bin/install -g postgres -m 775 -d /run/postgresql  
RUN /usr/bin/install -o postgres -d /var/log/postgres  
  
VOLUME ["/ssl", "/backup", "/srv/http"]  
  
ADD oc-install /usr/local/bin/oc-install  
ADD oc-perms /usr/local/bin/oc-perms  
ADD oc-backup /usr/local/bin/backup  
ADD occ /usr/local/bin/occ  
ADD httpd-vhosts.conf /etc/httpd/conf/extra/httpd-vhosts.conf  
ADD server.key /ssl/server.key  
ADD server.crt /ssl/server.crt  
  
EXPOSE 80  
EXPOSE 433  
WORKDIR /srv/http/  
  
ENTRYPOINT ["oc-install"]  
CMD ["/usr/bin/apachectl", "start", "-DFOREGROUND"]  


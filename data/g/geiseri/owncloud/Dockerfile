FROM debian:8.0  
MAINTAINER Ian Reinhart Geiser <geiseri@yahoo.com>  
  
EXPOSE 80 443  
ENV DEBIAN_FRONTEND noninteractive  
ENV container docker  
ENV OC_VERSION 9.0.2  
# early packages  
RUN apt-get update && \  
apt-get install -y curl perl  
  
# get owncloud  
RUN curl -L
http://download.owncloud.org/download/repositories/9.0/Debian_8.0/Release.key
| apt-key add - && \  
echo 'deb http://download.owncloud.org/download/repositories/9.0/Debian_8.0/
/' >> /etc/apt/sources.list.d/owncloud.list  
  
# setup debian  
RUN \  
apt-get update && \  
apt-get install -y \  
cron locales bzip2 php5-cli php5-gd php5-curl php5-intl \  
php5-mcrypt php5-ldap php5-gmp php5-apcu php5-imagick \  
php5 smbclient unzip \  
apache2 owncloud aria2 cloud-init \  
libapache2-mod-php5  
  
ADD owncloud/cron.conf /etc/cron.d/owncloud  
ADD owncloud/php.ini /etc/php5/apache2/conf.d/20-owncloud.ini  
ADD owncloud/owncloud.conf /etc/apache2/sites-available/owncloud.conf  
ADD owncloud/site.conf /etc/apache2/sites-available/000-default.conf  
ADD owncloud/occ.sh /usr/bin/occ  
RUN chmod +x /usr/bin/occ  
  
# Install ocDownloader  
ADD http://github.com/DjazzLab/ocdownloader/archive/master.zip /master.zip  
ADD https://yt-dl.org/downloads/2015.07.07/youtube-dl /usr/local/bin/youtube-
dl  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv ocdownloader-master
ocdownloader && rm -f /master.zip  
  
# Install Passwords  
ADD https://github.com/fcturner/passwords/archive/master.zip /master.zip  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv passwords-master/
passwords && rm -f /master.zip  
  
# Install Notes  
ADD https://github.com/owncloud/notes/archive/master.zip /master.zip  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv notes-master/ notes
&& rm -f /master.zip  
  
# Install MP3 Player  
ADD https://github.com/libasys/audios/archive/master.zip /master.zip  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv audios-master/ audios
&& rm -f /master.zip  
  
# Install bookmarks  
ADD https://github.com/owncloud/bookmarks/archive/master.zip /master.zip  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv bookmarks-master/
bookmarks && rm -f /master.zip  
  
# Install files_move  
ADD https://github.com/eotryx/oc_files_mv/archive/master.zip /master.zip  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv oc_files_mv-master/
files_mv && rm -f /master.zip  
  
# Install files_markdown  
ADD https://github.com/icewind1991/owncloud-markdown/archive/master.zip
/master.zip  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv files_markdown-
master/ files_markdown && rm -f /master.zip  
  
# Install calender  
ADD https://github.com/owncloud/calendar/archive/master.zip /master.zip  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv calendar-master/
calendar && rm -f /master.zip  
  
# Install tasks  
ADD https://github.com/owncloud/tasks/archive/master.zip /master.zip  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv tasks-master/ tasks
&& rm -f /master.zip  
  
# Install contacts  
ADD https://github.com/owncloud/contacts/archive/master.zip /master.zip  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv contacts-master/
contacts && rm -f /master.zip  
  
# Install mail  
ADD https://github.com/owncloud/mail/archive/master.zip /master.zip  
RUN cd /var/www/owncloud/apps && unzip /master.zip && mv mail-master/ mail &&
rm -f /master.zip  
  
# fix perms  
RUN chown www-data:www-data /var/www/owncloud/apps  
  
# systemd  
ADD systemd/aria2.service /lib/systemd/system/aria2.service  
ADD systemd/systemd-tmpfiles-setup.service /etc/systemd/system/systemd-
tmpfiles-setup.service.d/ignoresysfs.conf  
ADD systemd/limits.conf /etc/security/limits.conf  
  
# cloud init  
ADD cloud-init/cloud.cfg /etc/cloud/cloud.cfg  
ADD cloud-init/user-data /var/lib/cloud/seed/nocloud/user-data  
ADD cloud-init/meta-data /var/lib/cloud/seed/nocloud/meta-data  
ADD cloud-init/first-run.sh /usr/bin/first-run.sh  
RUN chmod +x /usr/bin/first-run.sh  
  
RUN a2enmod headers rewrite env dir mime setenvif ssl php5  
RUN a2ensite default-ssl  
  
# clean up apt  
RUN apt-get -y clean && \  
apt-get autoremove -y --purge && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME [ "/var/www/owncloud/data", "/sys/fs/cgroup" ]  
  
# clean up systemd  
RUN \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ "$i" !=
"systemd-tmpfiles-setup.service" ] && rm -fv $i; done); \  
rm -fv /lib/systemd/system/multi-user.target.wants/*; \  
rm -fv /etc/systemd/system/*.wants/*; \  
rm -fv /lib/systemd/system/local-fs.target.wants/*; \  
rm -fv /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -fv /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -fv /lib/systemd/system/basic.target.wants/*; \  
systemctl enable cloud-init.service && \  
systemctl enable cloud-config.service && \  
systemctl enable cloud-final.service && \  
systemctl disable mysql.service && \  
systemctl enable aria2.service && \  
systemctl enable cron.service && \  
systemctl set-default multi-user.target && \  
useradd --system -U syslog  
  
WORKDIR /var/www/owncloud  
  
CMD ["/lib/systemd/systemd"]  


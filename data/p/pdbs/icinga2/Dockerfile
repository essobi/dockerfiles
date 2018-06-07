FROM ubuntu:latest  
LABEL build="201801122105"  
LABEL maintainer "marc.jakob@bs.ch"  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
apt-get update && \  
apt-get -y install locales && \  
locale-gen en_US.UTF-8 && \  
locale-gen de_CH.UTF-8 && \  
locale-gen de_DE.UTF-8 && \  
update-locale && \  
echo "deb http://packages.icinga.org/ubuntu icinga-xenial main" >>
/etc/apt/sources.list.d/icinga.list && \  
echo "deb-src http://packages.icinga.org/ubuntu icinga-xenial main" >>
/etc/apt/sources.list.d/icinga.list && \  
apt-key adv --fetch-keys http://packages.icinga.org/icinga.key && \  
apt-get update  
  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'
TZ='Europe/Zurich'  
  
COPY start.sh /  
  
RUN apt-get install postgresql apache2 -y && \  
rm -r /var/lib/postgresql/9.5/main && \  
mkdir -p /var/lib/postgresql/9.5/main && \  
chown postgres /var/lib/postgresql/9.5/main && \  
su - postgres -c "/usr/lib/postgresql/9.5/bin/initdb -D
/var/lib/postgresql/9.5/main -E UTF8 --locale=de_CH.utf8"  
  
COPY pg_hba.conf /etc/postgresql/9.5/main/  
  
RUN chown postgres:postgres /etc/postgresql/9.5/main/pg_hba.conf && \  
chmod 0640 /etc/postgresql/9.5/main/pg_hba.conf && \  
su - postgres -c "/usr/lib/postgresql/9.5/bin/pg_ctl -D
/var/lib/postgresql/9.5/main -l logfile start" && \  
apt-get install icinga2 nagios-plugins libapache2-mod-auth-kerb icingaweb2
libapache2-mod-php php php-pgsql php-gd icinga2-ido-pgsql postfix bsd-mailx -y
&& \  
apt-get --no-install-recommends install nagios-nrpe-plugin -y && \  
apt-get clean && \  
tar -cf /cfg.tar /var/www /etc/apache2 /etc/icinga2 /etc/icingaweb2
/var/lib/postgresql/9.5 && \  
rm -rf /var/www /etc/apache2 /etc/icinga2 /etc/icingaweb2
/var/lib/postgresql/9.5 \  
/var/lib/apt/lists/* /usr/share/doc /usr/share/man /usr/share/locale && \  
chmod 0750 /start.sh  
  
EXPOSE 80 443  
VOLUME ["/var/www", "/etc/apache2", "/var/log/apache2", "/etc/icinga2",
"/etc/icingaweb2", "/var/lib/postgresql/9.5" ]  
ENTRYPOINT ["/start.sh"]  


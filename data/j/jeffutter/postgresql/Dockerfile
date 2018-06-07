# Postgresql  
#  
# VERSION 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Jeffery Utter "jeff@jeffutter.com"  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen $LANG; echo "LANG=\"${LANG}\"" > /etc/default/locale; dpkg-
reconfigure locales  
  
# prevent apt from starting postgres right after the installation  
RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d; chmod +x
/usr/sbin/policy-rc.d  
  
RUN apt-get update ;\  
apt-get -y install wget vim-tiny  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list ;\  
wget --no-check-certificate --quiet -O -
https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
  
RUN apt-get update ;\  
apt-get -y install postgresql-9.3 postgresql-contrib-9.3  
  
# allow autostart again  
RUN rm /usr/sbin/policy-rc.d  
  
RUN echo 'host all all 0.0.0.0/0 md5' >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN ex -sc "%s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" -c
"x" /etc/postgresql/9.3/main/postgresql.conf ;\  
sed -i "s#/etc/ssl/certs/#/var/lib/postgresql/9.3/main/#"
/etc/postgresql/9.3/main/postgresql.conf ;\  
sed -i "s#/etc/ssl/private/#/var/lib/postgresql/9.3/main/#"
/etc/postgresql/9.3/main/postgresql.conf ;\  
cp /etc/ssl/certs/ssl-cert-snakeoil.pem /var/lib/postgresql/9.3/main/ ;\  
cp /etc/ssl/private/ssl-cert-snakeoil.key /var/lib/postgresql/9.3/main/ ;\  
chown -R postgres:postgres /var/lib/postgresql/9.3/main/ssl-cert-snakeoil.*  
  
EXPOSE 5432  
CMD ["su", "postgres", "sh", "-c", "/usr/lib/postgresql/9.3/bin/postgres -D
/var/lib/postgresql/9.3/main -c
config_file=/etc/postgresql/9.3/main/postgresql.conf"]  


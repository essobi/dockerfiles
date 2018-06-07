FROM ubuntu:latest  
  
MAINTAINER Daniel Binggeli <db@xbe.ch>  
  
#15.02.2015 Update to Kivitendo 3.2  
# parameter  
# Change this values to your preferences  
ENV postgresversion 9.5  
ENV locale de_DE  
ENV postrespassword docker  
  
  
  
  
#Packages  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get -qq update && apt-get -y upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \  
apt-get -y install apache2 libarchive-zip-perl libclone-perl \  
libconfig-std-perl libdatetime-perl libdbd-pg-perl libdbi-perl \  
libemail-address-perl libemail-mime-perl libfcgi-perl libjson-perl \  
liblist-moreutils-perl libnet-smtp-ssl-perl libnet-sslglue-perl \  
libparams-validate-perl libpdf-api2-perl librose-db-object-perl \  
librose-db-perl librose-object-perl libsort-naturally-perl libpq5 \  
libstring-shellquote-perl libtemplate-perl libtext-csv-xs-perl \  
libtext-iconv-perl liburi-perl libxml-writer-perl libyaml-perl \  
libfile-copy-recursive-perl postgresql git build-essential \  
libgd-gd2-perl libimage-info-perl sed supervisor libgd-gd2-perl  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install language-pack-de-base  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install sudo  
  
#Install missing Perl Modules  
RUN cpan HTML::Restrict  
RUN cpan Image::Info  
  
# ADD KIVITENDO  
# Kivitendo intallation  
RUN git clone https://github.com/kivitendo/kivitendo-erp.git
/var/www/kivitendo-erp  
RUN cd /var/www/kivitendo-erp && git checkout release-3.2.0  
ADD kivitendo.conf /var/www/kivitendo-erp/config/kivitendo.conf  
  
#Check Kivitendo installation  
RUN cd /var/www/kivitendo-erp/ && perl /var/www/kivitendo-
erp/scripts/installation_check.pl  
  
# ADD POSTGRES  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
# Add PostgreSQL's repository. It contains the most recent stable release  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
# Install ``python-software-properties``, ``software-properties-common`` and
PostgreSQL  
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&\  
apt-get install -y python-software-properties software-properties-common \  
postgresql-${postgresversion} postgresql-client-${postgresversion} postgresql-
contrib-${postgresversion}  
  
# Run the rest of the commands as the ``postgres`` user created by the
``postgres-${postgresversion}`` package when it was ``apt-get installed``  
USER postgres  
  
# Set the locale of the db cluster  
RUN pg_dropcluster --stop ${postgresversion} main && pg_createcluster --locale
${locale}.UTF-8 --start ${postgresversion} main  
  
# Create a PostgreSQL role named ``docker`` with ``docker`` as the password
and  
# then create a database `docker` owned by the ``docker`` role.  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER docker WITH SUPERUSER PASSWORD
'${postrespassword}';" &&\  
psql --command "CREATE USER kivitendo WITH SUPERUSER PASSWORD
'${postrespassword}';" &&\  
createdb -O docker docker &&\  
createdb -O kivitendo kivitendo  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >>
/etc/postgresql/${postgresversion}/main/pg_hba.conf  
  
# And add ``listen_addresses`` to
``/etc/postgresql/${postgresversion}/main/postgresql.conf``  
RUN sed -ri "s/^#(listen_addresses\s*=\s*)\S+/\1'*'/"
"/etc/postgresql/${postgresversion}/main/postgresql.conf"  
  
RUN service postgresql restart  
  
# Expose the PostgreSQL port  
EXPOSE 5432  
# ADD APACHE  
# Run the rest of the commands as the ``root`` user  
USER root  
  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd  
  
# SET Servername to localhost  
RUN echo "ServerName localhost" >> /etc/apache2/conf-available/servername.conf  
RUN a2enconf servername  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
RUN chown -R www-data:www-data /var/www  
RUN chmod u+rwx,g+rx,o+rx /var/www  
RUN find /var/www -type d -exec chmod u+rwx,g+rx,o+rx {} +  
RUN find /var/www -type f -exec chmod u+rw,g+rw,o+r {} +  
  
#Kivitendo rights  
RUN mkdir /var/www/kivitendo-erp/webdav  
RUN chown -R www-data /var/www/kivitendo-erp/users /var/www/kivitendo-
erp/spool /var/www/kivitendo-erp/webdav  
RUN chown www-data /var/www/kivitendo-erp/templates /var/www/kivitendo-
erp/users  
RUN chmod -R +x /var/www/kivitendo-erp/  
  
#Perl Modul im Apache laden  
RUN a2enmod cgi.load  
  
EXPOSE 80  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql",
"/var/log/apache2"]  
  
# Scripts  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD supervisord-apache2.sh /usr/local/bin/supervisord-apache2.sh  
ADD supervisord-postgresql.conf /etc/supervisor/conf.d/supervisord-
postgresql.conf  
ADD supervisord-postgresql.sh /usr/local/bin/supervisord-postgresql.sh  
ADD start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/*.sh  
  
# By default, simply start apache.  
CMD ["/usr/local/bin/start.sh"]  
  


FROM ubuntu:trusty  
MAINTAINER santail <nikolai.muhhin@gmail.com>  
  
ENV POSTGRES_VERSION 9.3  
# Installing packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-common
supervisor apache2 php5 curl && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main
$POSTGRES_VERSION" > /etc/apt/sources.list.d/pgdg.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install postgresql-$POSTGRES_VERSION
postgresql-client-$POSTGRES_VERSION postgresql-contrib-$POSTGRES_VERSION
php5-pgsql && \  
apt-get clean && \  
echo "host all all 0.0.0.0/0 md5" >>
/etc/postgresql/$POSTGRES_VERSION/main/pg_hba.conf && \  
echo "listen_addresses='*'" >>
/etc/postgresql/$POSTGRES_VERSION/main/postgresql.conf  
  
# Scripts  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD supervisord-apache2.sh /supervisord-apache2.sh  
ADD supervisord-postgresql.conf /etc/supervisor/conf.d/supervisord-
postgresql.conf  
ADD supervisord-postgresql.sh /supervisord-postgresql.sh  
ADD start.sh /start.sh  
RUN chmod 755 /*.sh  
  
#checkout application to working directory  
RUN mkdir -p /home/skype-applience-application.com && curl -sSL
https://github.com/santail/rest-api-sample-app-php/archive/master.tar.gz | tar
-xzv -C /home/skype-applience-application.com && \  
rm -fr /var/www/html && ln -s /home/skype-applience-application.com
/var/www/html && \  
mkdir -p /var/lib/postgresql && mkdir -p /var/log/postgresql  
  
VOLUME ["/var/log/postgresql", "/var/lib/postgresql"]  
  
EXPOSE 80 5432  
CMD ["/start.sh"]


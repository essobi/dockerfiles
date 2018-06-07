# Set the base image to Debian  
FROM debian:wheezy  
  
# File Author / Maintainer  
MAINTAINER opensource.knihovna.cz  
  
ENV REFRESHED_AT 2014-10-03  
ENV PATH /usr/bin:/bin:/usr/sbin:/sbin  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && apt-get -y install wget  
  
ADD koha.list /etc/apt/sources.list.d/koha.list  
RUN wget -O- http://debian.koha-community.org/koha/gpg.asc | apt-key add -  
RUN apt-get -y update && apt-get -y install koha-common && /etc/init.d/koha-
common stop  
  
RUN a2enmod rewrite  
  
RUN sed 's/INTRAPORT="80"/INTRAPORT="8080"/' /etc/koha/koha-sites.conf > koha-
sites.conf && \  
mv koha-sites.conf /etc/koha/koha-sites.conf  
RUN echo "Listen 8080 " >> /etc/apache2/ports.conf  
  
RUN apt-get -y update && apt-get -y install mysql-server gcc  
RUN /etc/init.d/mysql start; sleep 10; koha-create --create-db knihovna;
/etc/init.d/koha-common stop; /etc/init.d/apache2 stop; /etc/init.d/mysql
stop; sleep 10  
  
RUN koha-translate --install cs-CZ;  
RUN rm /etc/apache2/sites-enabled/000-default  
  
RUN sed 's/ServerName .*//' /etc/apache2/sites-enabled/knihovna.conf >
knihovna.conf && \  
mv knihovna.conf /etc/apache2/sites-enabled/knihovna.conf  
  
RUN apt-get -y install make  
RUN perl -MCPAN -e 'install Data::Pagination' && \  
perl -MCPAN -e 'upgrade Archive::Extract' && \  
perl -MCPAN -e 'upgrade Test::WWW::Mechanize' && \  
perl -MCPAN -e 'install HTTPD::Bench::ApacheBench'  
  
ADD import.sql /import.sql  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT /docker-entrypoint.sh  


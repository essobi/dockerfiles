FROM ubuntu:14.04  
MAINTAINER Team Pulpitum <teampulpitum@os.uk>  
#Originally from https://github.com/helvalius/nominatim-docker  
#Usage: docker run -e PG_DSN=pgsql://username:password@domain:port/database -p
8080:8080 nominatim-runner  
RUN apt-get update \  
&& apt-get -y install build-essential gcc git osmosis libxml2-dev libgeos-dev
libpq-dev libbz2-dev libtool cmake libproj-dev proj-bin libgeos-c1
libgeos++-dev libexpat1-dev autoconf make g++ libboost-dev libboost-system-dev
libboost-filesystem-dev libboost-thread-dev lua5.2 liblua5.2-dev php5 php-pear
php5-pgsql php5-json php-db bc apache2 libprotobuf-c0-dev protobuf-c-compiler
wget postgresql postgresql-server-dev-9.3 \  
&& apt-get clean \  
&& rm -rf /var/cache/*  
  
RUN mkdir -p /app/git/  
RUN git clone \--recursive --depth 1 https://github.com/twain47/Nominatim.git
/app/git/  
RUN mkdir -p /app/nominatim  
  
WORKDIR /app/nominatim  
  
RUN cmake /app/git/  
RUN make website  
RUN echo "<?php\n@define('CONST_Postgresql_Version',
'$POSTGRESQL_VER');\n@define('CONST_Postgis_Version', '$POSTGIS_VER');\n?>" >
/app/nominatim/settings/local.php  
  
WORKDIR /app/nominatim  
  
RUN mkdir -p /var/www/nominatim  
RUN ./utils/setup.php --create-website /var/www/nominatim  
  
ADD 400-nominatim.conf /etc/apache2/sites-available/400-nominatim.conf  
RUN a2enmod headers && \  
service apache2 start && \  
a2ensite 400-nominatim.conf && \  
/etc/init.d/apache2 reload  
  
EXPOSE 8080  
ADD start.sh /app/nominatim/start.sh  
RUN chmod +x /app/nominatim/start.sh  
  
CMD /app/nominatim/start.sh  


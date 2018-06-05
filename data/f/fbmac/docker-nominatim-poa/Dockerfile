FROM phusion/baseimage  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends php5 php5-mysql php5-gd
imagemagick unzip curl build-essential  
RUN apt-get install -y --no-install-recommends build-essential libxml2-dev
libgeos-dev libpq-dev libbz2-dev libtool automake libproj-dev libboost-dev
libboost-system-dev libboost-filesystem-dev libboost-thread-dev libexpat-dev
gcc proj-bin libgeos-c1 osmosis libgeos++-dev php5 php-pear php5-pgsql
php5-json php-db libprotobuf-c0-dev protobuf-c-compiler  
RUN apt-get install -y --no-install-recommends postgresql postgis postgresql-
contrib postgresql-9.3-postgis-2.1 postgresql-server-dev-9.3  
RUN pear install pear/DB  
  
RUN echo "fsync=off" >> /etc/postgresql/9.3/main/postgresql.conf  
RUN service postgresql start && \  
sudo -u postgres createuser -s root && \  
bash -c "psql postgres <<< \"UPDATE pg_database SET datistemplate = FALSE
WHERE datname = 'template1';\"" && \  
bash -c "psql postgres <<< \"DROP DATABASE template1;\"" && \  
bash -c "psql postgres <<< \"CREATE DATABASE template1 WITH TEMPLATE =
template0 ENCODING = 'UTF-8';\"" && \  
bash -c "psql postgres <<< \"alter user root with password 'root';\""  
  
ADD porto-alegre.osm.pbf /root/  
  
RUN curl -sSL http://www.nominatim.org/release/Nominatim-2.4.0.tar.bz2 | tar
xj && mv Nominatim-2.4.0 src  
RUN cd src && ./configure && make && make install  
RUN echo "<?php" > /src/settings/local.php  
RUN echo " @define('CONST_Database_DSN',
'pgsql://root:root@127.0.0.1/nominatim');" >> /src/settings/local.php  
  
RUN sudo service postgresql start && src/utils/setup.php --osm-file
/root/porto-alegre.osm.pbf --all  
RUN service postgresql start && src/utils/specialphrases.php --countries |
psql -d nominatim  
RUN sed -i 's/#ServerName.*$/ServerName localhost/' /etc/apache2/sites-
enabled/000-default.conf  
RUN mkdir /var/www/html/nominatim && chown www-data /var/www/html/nominatim  
RUN echo " @define('CONST_Website_BaseURL', 'http://localhost/nominatim/');"
>> /src/settings/local.php  
RUN service postgresql start && src/utils/setup.php --create-website
/var/www/html/nominatim && service postgresql stop  
  
RUN mkdir -p /etc/service/postgresql && echo "#!/bin/bash" >
/etc/service/postgresql/run && echo 'su -c
"/usr/lib/postgresql/9.3/bin/postgres -D /var/lib/postgresql/9.3/main -c
config_file=/etc/postgresql/9.3/main/postgresql.conf" postgres' >>
/etc/service/postgresql/run && mkdir -p /etc/service/apache && echo
"#!/bin/bash" > /etc/service/apache/run && echo "apachectl -DFOREGROUND" >>
/etc/service/apache/run && chmod a+x /etc/service/postgresql/run
/etc/service/apache/run  
  
EXPOSE 80  


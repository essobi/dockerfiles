FROM ubuntu:16.04  
# installation of nominatim for ubuntu 16: http://nominatim.org/release-
docs/latest/appendix/Install-on-Ubuntu-16/  
RUN apt-get update && \  
apt-get install -y build-essential cmake g++ libboost-dev libboost-system-dev
\  
libboost-filesystem-dev libexpat1-dev zlib1g-dev libxml2-dev\  
libbz2-dev libpq-dev libproj-dev \  
postgresql-server-dev-9.5 postgresql-9.5-postgis-2.2 \  
postgresql-contrib-9.5 \  
apache2 php php-pgsql libapache2-mod-php php-pear php-db \  
php-intl \  
python3-setuptools python3-dev python3-pip \  
python3-psycopg2 python3-tidylib phpunit php-cgi \  
python-pip python-gdal unzip libboost-all-dev \  
wget && \  
pear install PHP_CodeSniffer && \  
pip install osmium && \  
wget https://nominatim.org/release/Nominatim-3.1.0.tar.bz2 && \  
tar xf Nominatim-3.1.0.tar.bz2 -C / && \  
rm -f Nominatim-3.1.0.tar.bz2 && \  
mv Nominatim-3.1.0 /nominatim && \  
cd /nominatim && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make  
  
# add nominatim apache config  
COPY ./nominatim.conf /etc/apache2/conf-available/  
RUN a2enconf nominatim  
  
# copy settings and entrypoint  
COPY ./local.php /nominatim/build/settings/  
COPY ./docker-entrypoint.sh /  
  
ENV PGHOST postgis  
ENV PGUSER www-data  
ENV PGPASSWORD password  
ENV PGDATABASE nominatim  
  
VOLUME [ "/data" ]  
  
EXPOSE 80  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD [ ]  


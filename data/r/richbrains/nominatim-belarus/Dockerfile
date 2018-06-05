FROM ubuntu:xenial  
  
ENV USERNAME nominatim  
ENV USERHOME /app  
  
RUN apt-get -y update --fix-missing && \  
apt-get -y install wget && \  
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt xenial-pgdg main" >>
/etc/apt/sources.list' && \  
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-
key add - && \  
apt-get -y update  
  
RUN apt-get -y -f install postgresql-9.6 sudo \  
postgresql-server-dev-9.6 postgresql-9.6-postgis-2.3 postgresql-contrib-9.6
postgresql-9.6-postgis-scripts \  
curl build-essential cmake g++ libboost-dev libboost-system-dev \  
libboost-filesystem-dev libexpat1-dev zlib1g-dev libxml2-dev\  
libbz2-dev libpq-dev libgeos-dev libgeos++-dev libproj-dev \  
apache2 php php-pgsql libapache2-mod-php php-pear php-db \  
python-setuptools libboost-python-dev libexpat1-dev zlib1g-dev libbz2-dev \  
php-intl git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* /var/tmp/*  
  
WORKDIR /app  
  
RUN echo "host all all 0.0.0.0/0 trust" >>
/etc/postgresql/9.6/main/pg_hba.conf && \  
echo "listen_addresses='*'" >> /etc/postgresql/9.6/main/postgresql.conf  
  
RUN wget http://www.nominatim.org/release/Nominatim-3.0.1.tar.bz2 && tar xf
Nominatim-3.0.1.tar.bz2  
RUN mv Nominatim-3.0.1 Nominatim && cd Nominatim && mkdir build && cd build &&
cmake .. && make  
  
COPY local.php ./Nominatim/build/settings/local.php  
  
COPY nominatim.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN sudo easy_install pip && pip install osmium  
  
ENV PBF_DATA
https://download.bbbike.org/osm/extract/planet_26.782,53.563_28.345,54.241.osm.pbf  
RUN curl -L $PBF_DATA \--create-dirs -o /app/Nominatim/data.osm.pbf  
RUN service postgresql start && \  
sudo -u postgres psql postgres -tAc "SELECT 1 FROM pg_roles WHERE
rolname='nominatim'" | grep -q 1 || sudo -u postgres createuser -s nominatim
&& \  
sudo -u postgres psql postgres -tAc "SELECT 1 FROM pg_roles WHERE
rolname='www-data'" | grep -q 1 || sudo -u postgres createuser -SDR www-data
&& \  
useradd -m -p password1234 nominatim && \  
chown -R nominatim:nominatim ./Nominatim && \  
sudo -u nominatim ./Nominatim/build/utils/setup.php --osm-file
/app/Nominatim/data.osm.pbf --all --threads 2 && \  
sudo -u nominatim ./Nominatim/build/utils/update.php --init-updates && \  
service postgresql stop  
  
EXPOSE 5432  
EXPOSE 8080  
COPY start.sh /app/start.sh  
CMD /app/start.sh  


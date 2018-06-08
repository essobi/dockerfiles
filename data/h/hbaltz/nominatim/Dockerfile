FROM ubuntu:trusty  
MAINTAINER Hugo BALTZ <hugobaltz@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
  
# Install packages
http://wiki.openstreetmap.org/wiki/Nominatim/Installation#Ubuntu.2FDebian  
RUN apt-get -y update --fix-missing && \  
apt-get install -y build-essential libxml2-dev libpq-dev libbz2-dev libtool
automake \  
libproj-dev libboost-dev libboost-system-dev libboost-filesystem-dev \  
libboost-thread-dev libexpat-dev gcc proj-bin libgeos-c1 libgeos++-dev \  
libexpat-dev php5 php-pear php5-pgsql php5-json php-db libapache2-mod-php5 \  
postgresql postgis postgresql-contrib postgresql-9.3-postgis-2.1 \  
postgresql-server-dev-9.3 curl git autoconf-archive cmake python \  
lua5.1 liblua5.1-dev libluabind-dev \  
osmosis && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* /var/tmp/*  
  
WORKDIR /app  
  
# Configure postgres  
RUN echo "host all all 0.0.0.0/0 trust" >>
/etc/postgresql/9.3/main/pg_hba.conf && \  
echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# Nominatim install  
ENV NOMINATIM_VERSION v.2.5.0  
RUN git clone \--recursive git://github.com/twain47/Nominatim.git ./src  
RUN cd ./src && git checkout $NOMINATIM_VERSION && git submodule update
--recursive --init && \  
./autogen.sh && ./configure && make  
  
# Nominatim create site  
COPY local.php ./src/settings/local.php  
RUN rm -rf /var/www/html/* && ./src/utils/setup.php --create-website
/var/www/html  
  
# Apache configure  
COPY nominatim.conf /etc/apache2/sites-enabled/000-default.conf  
  
EXPOSE 5432  
EXPOSE 8080


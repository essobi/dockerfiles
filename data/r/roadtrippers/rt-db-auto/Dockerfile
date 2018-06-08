FROM phusion/baseimage:0.9.11  
MAINTAINER davidstacy  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
  
RUN export LANGUAGE=en_US.UTF-8 \  
&& export LANG=en_US.UTF-8 \  
&& locale-gen --no-purge en_US.UTF-8 \  
&& update-locale LANG=en_US.UTF-8 \  
&& export LC_ALL=en_US.UTF-8  
  
RUN sudo apt-get update -y \  
&& sudo apt-get install -y ca-certificates wget pwgen inotify-tools \  
&& sudo wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add - \  
&& sudo echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list \  
&& sudo apt-get update -y  
  
RUN sudo apt-get update -y && \  
sudo apt-get install -y \  
libgdal-dev \  
libspatialite-dev \  
libgeos-dev \  
liblwgeom-dev \  
&& sudo apt-get install -y \  
build-essential \  
postgresql-9.2 \  
postgresql-server-dev-9.2 \  
postgresql-contrib-9.2 \  
libxml2-dev \  
libproj-dev \  
libjson0-dev \  
xsltproc \  
docbook-xsl \  
docbook-mathml \  
&& sudo /etc/init.d/postgresql stop  
  
  
# you must install postgis 2.0 manually because of a warning that pops up and
breaks the run script  
RUN wget http://download.osgeo.org/postgis/source/postgis-2.0.6.tar.gz \  
&& tar xfz postgis-2.0.6.tar.gz  
RUN cd postgis-2.0.6 \  
&& ./configure \  
&& make \  
&& sudo make install \  
&& sudo ldconfig \  
&& sudo make comments-install \  
&& rm /postgis-2.0.6.tar.gz  
  
#Lastly, enable the command-line tools to work from your shell:  
RUN sudo ln -sf /usr/share/postgresql-common/pg_wrapper
/usr/local/bin/shp2pgsql \  
&& sudo ln -sf /usr/share/postgresql-common/pg_wrapper
/usr/local/bin/pgsql2shp \  
&& sudo ln -sf /usr/share/postgresql-common/pg_wrapper
/usr/local/bin/raster2pgsql  
  
RUN sudo apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# setup data directory  
RUN sed -i -e"s/data_directory =.*$/data_directory = '\/db'/"
/etc/postgresql/9.2/main/postgresql.conf  
  
# allow connections from anywhere  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.2/main/pg_hba.conf  
RUN echo "listen_addresses = '*'" >> /etc/postgresql/9.2/main/postgresql.conf  
RUN echo "port = 5432" >> /etc/postgresql/9.2/main/postgresql.conf  
  
EXPOSE 5432  
ADD scripts /scripts  
RUN chmod +x /scripts/start.sh  
RUN touch /firstrun  
  
RUN mkdir /etc/service/postgresql  
RUN ln -s /scripts/start.sh /etc/service/postgresql/run  
  
VOLUME ["/db", "/var/log/postgresql", "/etc/postgresql"]  
  
CMD ["/sbin/my_init"]  


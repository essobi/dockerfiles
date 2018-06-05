FROM debian:stretch  
MAINTAINER Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
RUN apt-get update  
RUN apt-get -q -y -o Dpkg::Options::=--force-confdef -o
Dpkg::Options::=--force-confold --purge install postgresql postgis unzip curl  
COPY preparedb.sh /tmp/preparedb.sh  
  
# This will retrieve the shapes file directly from naturalearthdata.  
#  
RUN curl -LO
http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries_lakes.zip  
  
# Use the locally provided ne_110m_admin_0_countries_lakes.shp file.  
# COPY ne_110m_admin_0_countries_lakes.zip ne_110m_admin_0_countries_lakes.zip  
RUN unzip ne_110m_admin_0_countries_lakes.zip  
RUN shp2pgsql -W "latin1" ne_110m_admin_0_countries_lakes.shp geoborders >>
geoborders.sql  
RUN sh /tmp/preparedb.sh  
RUN sed -i -e "s/^#.*listen_addresses.*=.*'.*'/listen_addresses = '*'/g"
/etc/postgresql/9.6/main/postgresql.conf  
  
# Disable shared memory since that doesn't work well in Docker.  
RUN sed -i -e "s/^dynamic_shared_memory_type.*=.*$/dynamic_shared_memory_type
= none/g" /etc/postgresql/9.6/main/postgresql.conf  
  
RUN echo "host\tgis\tgeoreader\t0.0.0.0/0\tmd5" >>
/etc/postgresql/9.6/main/pg_hba.conf  
RUN echo "host\tgis\tgeoreader\t::/0\tmd5" >>
/etc/postgresql/9.6/main/pg_hba.conf  
  
EXPOSE 5432/tcp  
  
CMD ["su", "postgres", "-c", "/usr/lib/postgresql/9.6/bin/postmaster -D
/var/lib/postgresql/9.6/main -c
config_file=/etc/postgresql/9.6/main/postgresql.conf < /dev/null"]  


FROM rocker/shiny  
  
MAINTAINER Stefan Fritsch <stefan.fritsch@stat-up.com>  
  
RUN apt-get update  
RUN apt-get -o Dpkg::Options::="--force-confold" install -y libssl-dev apt-
utils libxml2-dev  
  
RUN apt-get install -y --no-install-recommends \  
icedtea-netx \  
libgdal-dev \  
libproj-dev \  
libgeos-dev \  
libgsl0-dev \  
librsvg2-dev \  
libxcb1-dev \  
libxdmcp-dev \  
libxslt1-dev \  
libxt-dev \  
mdbtools \  
netcdf-bin  
  
RUN apt-get -o Dpkg::Options::="--force-confold" install -y jags ed
libudunits2-dev libudunits2-0 dnsutils  
  
RUN apt-get -o Dpkg::Options::="--force-confold" install -y nano bzip2  
# fr_FR.UTF-8 locale is used by data.table to read .csv with dec=","  
RUN echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen \  
&& echo "de_DE.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen  
RUN update-locale  
  
RUN chmod -R 0777 /usr/local/lib/R  
  
RUN mkdir /home/shiny/.checkpoint  
RUN chown shiny:shiny /home/shiny/.checkpoint  
  
EXPOSE 3838  
CMD ["/usr/bin/shiny-server.sh"]  


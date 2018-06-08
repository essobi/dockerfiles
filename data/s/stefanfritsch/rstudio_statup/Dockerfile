FROM rocker/verse  
MAINTAINER Stefan Fritsch <fritsch@stat-up.com>  
  
RUN apt-get update  
RUN apt-get -o Dpkg::Options::="--force-confold" upgrade -y  
  
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
RUN apt-get -o Dpkg::Options::="--force-confold" install -y python-pip
python-h5py  
RUN apt-get -o Dpkg::Options::="--force-confold" install -y virtualenv  
  
# RUN apt-get autoremove -y  
# Miniconda  
# RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh  
# RUN bash Miniconda2-latest-Linux-x86_64.sh -b -f -p /opt/local/python  
# RUN rm Miniconda2-latest-Linux-x86_64.sh  
# RUN echo export PATH="/opt/local/python/bin:$PATH" >
/etc/profile.d/miniconda.sh  
# RUN chmod a+x /etc/profile.d/miniconda.sh  
# sed -i.bak 's/\\(PATH=)(.*\\)/\1\/opt\/local\/python\/bin\:\2/'
/usr/local/lib/R/etc/Renviron  
# echo TENSORFLOW_PYTHON=/opt/local/python/lib >>
/usr/local/lib/R/etc/Renviron  
# fr_FR.UTF-8 locale is used by data.table to read .csv with dec=","  
RUN pip install tensorflow  
RUN pip install keras  
  
RUN echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen \  
&& echo "de_DE.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen  
RUN update-locale  
  
# We can only share a site-library if we constantly fix the permissions -_-  
RUN chmod -R 0777 /usr/local/lib/R/site-library  
  
COPY permissions-cron.sh /etc/services.d/permissions-cron/run  
# Finalize and clean-up  
RUN apt-get clean  
  
EXPOSE 8787  
  
WORKDIR /  
  
CMD ["/init"]  


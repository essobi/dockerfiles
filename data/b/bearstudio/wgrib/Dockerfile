FROM docker.io/debian:jessie  
  
MAINTAINER BearStudio <contact@bearstudio.fr>  
  
ENV FILE_TYPE ""  
ENV LINK_FILE_TO_DOWNLOAD ""  
ENV GRIB_PARAMS ""  
ENV ROUTING_KEY_PARSE_PREFIX ""  
ENV GRIB_POSITION ""  
ENV OTHER ""  
ENV DEBUG true  
  
# Install script dependance avaible on apt source  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
wget \  
build-essential \  
bzip2 \  
tar \  
amqp-tools \  
openssh-client \  
gfortran \  
\--no-install-recommends && rm -r /var/lib/apt/lists/* && \  
wget ftp://ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2.tgz.v2.0.4 -O
/tmp/wgrib2.tgz && \  
mkdir -p /usr/local/grib2/ && \  
cd /tmp/ && \  
tar -xf /tmp/wgrib2.tgz && \  
rm -r /tmp/wgrib2.tgz && \  
mv /tmp/grib2/ /usr/local/grib2/ &&\  
cd /usr/local/grib2/grib2 && \  
make && \  
ln -s /usr/local/grib2/grib2/wgrib2/wgrib2 /usr/local/bin/wgrib2 && \  
apt-get -y autoremove build-essential  
  
WORKDIR /opt/  
VOLUME /srv/  
VOLUME /opt/  
  
CMD ["/opt/entrypoint.sh"]  


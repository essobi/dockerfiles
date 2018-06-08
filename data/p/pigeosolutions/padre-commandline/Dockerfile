FROM debian:stretch  
#FROM ubuntu:16.04  
MAINTAINER Jean Pommier "jp@pi-geosolutions.fr"  
#Gives a SSH access + several SIG & more general commandline tools : GDAL,
python with geospatial extensions  
# SSH part taken from https://hub.docker.com/r/macropin/sshd/  
# Also runs CRON  
# Uses supervisor in order to run side-by-side cron and sshd  
#install ssh server + system utilities  
RUN apt-get update && \  
apt-get install -y \  
cmake \  
cron \  
curl \  
dos2unix \  
git \  
locales \  
locate \  
openjdk-8-jre \  
openssh-server \  
p7zip-full \  
rsync \  
supervisor \  
tar \  
unzip \  
vim \  
wget \  
xsltproc \  
zip  
  
#install postgresql/postgis support, gdal, libgrib API  
# & python virtualenv that will be used by any user needing it to install its
specific python libs :  
# numpy, scipy, rasterstats
(http://pythonhosted.org/rasterstats/installation.html), statsmodel,  
# python-gdal is necessary to get gdal python tools such as gdal_edit.py  
RUN apt-get update && \  
apt-get install -y \  
gdal-bin \  
gfortran \  
libgdal20 \  
libgdal-dev \  
libgrib-api0 \  
postgis \  
postgresql-client \  
python \  
python-pip \  
python-gdal \  
python3-gdal \  
python3-pip \  
python3-venv \  
&& rm -rf /var/lib/apt/lists/* && apt-get clean \  
&& pip3 install --upgrade pip  
  
RUN mkdir -p ~root/.ssh /etc/authorized_keys && chmod 700 ~root/.ssh/ && \  
sed -i -e 's@^AuthorizedKeysFile.*@@g' /etc/ssh/sshd_config && \  
echo "AuthorizedKeysFile\t.ssh/authorized_keys /etc/authorized_keys/%u" >>
/etc/ssh/sshd_config && \  
cp -a /etc/ssh /etc/ssh.cache  
  
#Install grib tools  
##ecCodes (https://software.ecmwf.int/wiki/display/ECC/ecCodes+installation)  
RUN cd /var/lib && \  
wget
https://software.ecmwf.int/wiki/download/attachments/45757960/eccodes-2.5.0-Source.tar.gz?api=v2
-O - | tar -xz && \  
mkdir /var/lib/eccodesBuild ; cd /var/lib/eccodesBuild && \  
sed -i -e 's@set( ECCODES_EXTRA_INCLUDE_DIRS "" )@set(
ECCODES_EXTRA_INCLUDE_DIRS "/usr/include/openjpeg-2.1/" )@g'
/var/lib/eccodes-2.5.0-Source/CMakeLists.txt && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr/local ../eccodes-2.5.0-Source/ && \  
make && make install  
  
## wgrib2  
#ldconfig updates library paths, needed at least for eccodes  
RUN cd /var/lib && \  
wget ftp://ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2.tgz && \  
tar -xzf wgrib2.tgz ;rm wgrib2.tgz ; mv grib2 wgrib2 ; cd wgrib2 && \  
export CC=gcc && export FC=gfortran && \  
make && \  
echo "PATH=$PATH:/var/lib/wgrib2/wgrib2" >> /etc/profile && \  
ldconfig  
  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
#Set locale  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
&& localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias
fr_FR.UTF-8  
ENV LANG en_US.utf8  
  
EXPOSE 22  
#add user files skeleton for useradd (needed for custom bash prompt  
ADD etc/skel/* /etc/skel/  
  
ADD supervisord.conf /etc/supervisor/  
RUN mkdir -p /var/log/supervisor  
  
ADD entry.sh /entry.sh  
RUN chmod u+x /entry.sh  
  
ENTRYPOINT ["/entry.sh"]  
  
#CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  


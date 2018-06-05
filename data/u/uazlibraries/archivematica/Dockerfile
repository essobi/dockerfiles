#  
# Archivematica Dockerfile  
#  
# Instructions below capture instructions from:  
#  
# https://www.archivematica.org/en/docs/archivematica-1.6/admin-
manual/installation/installation/#advanced  
#  
# Pull base image, ubuntu 14.04 + oracle jdk8  
#FROM mlaccetti/docker-oracle-java8-ubuntu-16.04  
#FROM jared314/docker-ubuntu-14-04-java8  
FROM ubuntu:14.04  
  
# Logging for elasticsearch: /var/log/elasticsearch  
# Logging for gearman: /var/log/gearman-job-server  
# Logging nginx: www-data.adm:/var/log/nginx  
#RUN groupadd www-data --gid 330 && \  
#useradd www-data --uid 330 --gid 330 --create-home --home /var/lib/nginx
--shell /bin/false  
# Logging for clamav: /var/log/clamav  
# Logging for mysql: /var/log/mysql  
# Logging for archivematica: /var/log/archivematica, /var/log/fits-ngserver  
RUN \  
groupadd elasticsearch \--gid 328 && \  
useradd elasticsearch \--uid 328 \--gid 328 \--create-home \--home
/var/lib/elasticsearch \--shell /bin/false && \  
groupadd gearman \--gid 329 && \  
useradd gearman \--uid 329 \--gid 329 \--create-home \--home /var/lib/gearman
\--shell /bin/false && \  
groupadd clamav \--gid 331 && \  
useradd clamav \--uid 331 \--gid 331 \--create-home \--home /var/lib/clamav
\--shell /bin/false && \  
groupadd mysql \--gid 332 && \  
useradd mysql \--uid 332 \--gid 332 \--create-home \--home /var/lib/mysql
\--shell /bin/false && \  
groupadd archivematica \--gid 333 && \  
useradd archivematica \--uid 333 \--gid 333 \--create-home \--home
/var/archivematica \--shell /bin/false  
  
# Update apt sources to fastest local mirror  
RUN mv /etc/apt/sources.list /etc/apt/sources.list-archive.ubuntu.com  
COPY docker/sources.list-mirrors.os6.org /etc/apt/sources.list  
  
# Make apt-get commands temporarily non-interactive  
# Solution from https://github.com/phusion/baseimage-docker/issues/58  
# Update apt cache to use fastest local mirror  
RUN \  
echo 'debconf debconf/frontend select Noninteractive' | \  
debconf-set-selections && \  
apt-get update && \  
apt-get -y upgrade  
  
# Install useful utilities, apt https transport  
# oracle-java8-set-default oracle-java8-unlimited-jce-policy  
# default-jdk used by: elasticsearch, archivematica-mcp-client  
# mysql-server used by: archivematica-storage-service, archivematica-mcp-
server, archivematica-mcp-client  
# python-minimal gearmon used by: archivematica-storage-service,
archivematica-mcp-server  
# nginx used by archivematica-storage-service, dashboard  
# archivematica-mcp-server: rsync  
# archivematica-mcp-client deps: software-properties-common ffmpeg fits jhove
libxml2-dev pkg-config  
# archivematica-common: python-dev libmysqlclient-dev  
# archivematica-storage: unar  
# archivematica-dashboard: python-dateutil python-gearman python-simplejson  
RUN apt-get install -y apt-transport-https aptitude debconf-utils man time
less nano emacs vim wget curl sudo openjdk-7-jre-headless openjdk-7-jdk
software-properties-common python rsync gearman clamav-daemon nginx
libxml2-dev libxslt-dev python-dev libmysqlclient-dev default-jdk python-
dateutil python-gearman python-simplejson dbconfig-common libdbd-mysql-perl
libdbi-perl libffi-dev libgsm1 libhtml-template-perl libopenjpeg2 liborc-0.4-0
libossp-uuid16 libschroedinger-1.0-0 libssl-dev libssl-doc libterm-readkey-
perl libvo-aacenc0 libvo-amrwbenc0 libx264-142 libdbd-mysql-perl libdbi-perl
libffi-dev libgsm1 libhtml-template-perl libopenjpeg2 liborc-0.4-0 libossp-
uuid16 libschroedinger-1.0-0 libssl-dev libssl-doc libaio1 uuid  
  
# Add archivematica, archivematica-mcp-client deps mc3man, elasticsearch repo:  
RUN \  
echo "deb [arch=amd64] https://packages.archivematica.org/1.6.x/ubuntu trusty
main" >> /etc/apt/sources.list.d/archivematica-repo.list && \  
echo "deb [arch=amd64] https://packages.archivematica.org/1.6.x/ubuntu-
externals trusty main" >> /etc/apt/sources.list.d/archivematica-repo.list && \  
wget -O - https://packages.archivematica.org/1.6.x/key.asc | apt-key add \- &&
\  
add-apt-repository ppa:mc3man/trusty-media && \  
echo "deb http://packages.elasticsearch.org/elasticsearch/1.7/debian stable
main" >> /etc/apt/sources.list.d/elasticsearch-repo.list && \  
wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key
add \- && \  
apt-get update  
  
# Install elasticsearch, a ton of deps for archivematica-mcp-client  
RUN apt-get install -y unar ffmpeg fits jhove bagit atool bulk-extractor
clamav sleuthkit tesseract-ocr tika tree ufraw unrar-free p7zip-full pbzip2
libimage-exiftool-perl imagemagick inkscape mediainfo nailgun-client keyutils
readpst rpcbind siegfried postfix libxml2-utils logapp md5deep nfs-common
libvo-aacenc0 libvo-amrwbenc0 libx264-142 libavcodec-extra-56 libavutil54
libavcodec-extra-56 libswresample1  
# Update PIP:  
RUN \  
wget https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm -f get-pip.py  
# Download archivematica packages, for post-installation once the  
# docker container is running because a running db is required  
#RUN aptitude --download-only -y install \  
RUN apt-get install -d -y \  
mysql-server \  
elasticsearch \  
archivematica-storage-service \  
archivematica-mcp-server \  
archivematica-dashboard \  
archivematica-mcp-client  
  
# Restore apt-get commands to interactive  
# Create directory to add docker installation scripts  
# Create directories used to export volumes  
RUN echo 'debconf debconf/frontend select Teletype' | \  
debconf-set-selections && \  
mkdir -p /etc/archivematica/archivematicaCommon && \  
mkdir /var/log/archivematica && \  
chown -vR archivematica.archivematica /var/log/archivematica && \  
mkdir -p /run/archivematica && \  
chown -vR archivematica.archivematica /run/archivematica  
  
# Add docker installation scripts  
ADD docker/ /usr/share/archivematica/docker/  
# Move docker installation files to runtime locations  
# Install pre-downloaded clamav virus database.  
# Setup archivematica log directory  
RUN \  
mv /usr/share/archivematica/docker/init.d/archivematica-* /etc/init.d/ && \  
mv /usr/share/archivematica/docker/dbconfig-common/* /etc/dbconfig-common/ &&
\  
mv /usr/share/archivematica/docker/entrypoint-archivematica.sh /entrypoint-
archivematica.sh && \  
mv -v /usr/share/archivematica/docker/var.lib.clamav/* /var/lib/clamav && \  
chown -vR clamav.clamav  /var/lib/clamav && \  
rm -vfr /usr/share/archivematica/docker/var.lib.clamav  
  
#VOLUME [ "/var/lib/elasticsearch", "/var/lib/gearman", "/var/lib/clamav",
"/var/lib/mysql", "/var/archivematica", "/var/log",
"/usr/share/archivematica/dashboard", "/usr/share/python/archivematica-
storage-service", "/run/archivematica" ]  
EXPOSE 80 443 8000 8001 8002  
  
# Auto-start  
CMD /entrypoint-archivematica.sh restart FOREGROUND  


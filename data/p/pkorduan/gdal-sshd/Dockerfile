FROM debian:jessie  
  
MAINTAINER Peter Korduan <peter.korduan@gdi-service.de>  
LABEL version="2.3.2"  
  
ENV OS_USER="gisadmin" USER_DIR="/home/${OS_USER}" TZ="Europe/Berlin"
NOTVISIBLE="in users profile"  
USER root  
  
RUN sed -i \  
-e "s|# alias ls=|alias ls=|g" \  
-e "s|# alias ll=|alias ll=|g" \  
-e "s|# alias rm=|alias rm=|g" \  
~/.bashrc && \  
echo $TZ > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
gdb \  
git \  
less \  
libcurl4-gnutls-dev \  
libexpat1-dev \  
libpq-dev \  
libspatialite-dev \  
libxerces-c-dev \  
libxml2-dev \  
ntp \  
openssh-server \  
postgresql-client \  
subversion \  
zip  
  
WORKDIR /usr/local  
  
RUN svn checkout http://svn.osgeo.org/gdal/trunk/gdal  
  
WORKDIR /usr/local/gdal  
  
RUN ./configure --with-xerces --with-curl --with-xml2 --with-spatialite
--prefix=/usr/local/gdal --enable-debug  
RUN make  
RUN make install  
RUN echo /usr/local/gdal/lib >> /etc/ld.so.conf  
RUN ldconfig  
  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:secret' | chpasswd && \  
sed -i 's|PermitRootLogin without-password|PermitRootLogin yes|'
/etc/ssh/sshd_config && \  
sed 's|session\s*required\s*pam_loginuid.so|session optional
pam_loginuid.so|g' -i /etc/pam.d/sshd && \  
echo "export VISIBLE=now" >> /etc/profile  
  
RUN useradd -ms /bin/bash ${OS_USER} && \  
echo 'gisadmin:secret' | chpasswd && \  
usermod -G ${OS_USER} www-data && \  
mkdir -p ${USER_DIR}/.ssh && \  
chown -R ${OS_USER}.${OS_USER} ${USER_DIR}/.ssh  
  
RUN apt-get purge -y \  
subversion \  
build-essential \  
libpq-dev \  
libxerces-c-dev  
  
WORKDIR "/var/www/data"  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  


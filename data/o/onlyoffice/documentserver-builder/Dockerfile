FROM ubuntu:trusty  
MAINTAINER Ascensio System SIA <support@onlyoffice.com>  
  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8
DEBIAN_FRONTEND=noninteractive QT_SELECT=qt5  
  
RUN apt-get -y update && \  
apt-get install --force-yes -yq apt-transport-https locales software-
properties-common curl && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
locale-gen en_US.UTF-8 && \  
apt-get -y update && \  
apt-get install --force-yes -yq \  
autoconf \  
build-essential \  
createrepo \  
debhelper \  
debhelper \  
default-jre \  
dpkg-dev \  
dpkg-dev \  
git \  
libatk1.0-dev \  
libcairo2-dev \  
libcurl4-gnutls-dev \  
libgconf2-dev \  
libgdk-pixbuf2.0-dev \  
libglib2.0-dev \  
libgtkglext1-dev \  
libtool \  
libxml2-dev \  
libxss-dev \  
nodejs \  
p7zip-full \  
python-pip \  
qt5-default \  
qtchooser \  
sed \  
subversion \  
symlinks \  
wget && \  
npm install -g grunt-cli && \  
npm cache clean && \  
pip install awscli && \  
rm -rf /var/lib/apt/lists/*  
  
ADD build.sh /app/onlyoffice/build.sh  
  
VOLUME /var/lib/onlyoffice  
  
CMD bash -C '/app/onlyoffice/build.sh'  


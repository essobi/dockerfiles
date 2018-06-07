FROM nerelohw/docker-ubuntu:14.04  
  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8
DEBIAN_FRONTEND=noninteractive QT_SELECT=qt5  
  
##  
#https://github.com/onlyoffice-testing-robot/documentserver-from-source-
build/blob/master/Dockerfile-Ubuntu-16.04  
  
RUN apt-get -y update && apt-get install -yq locales software-properties-
common curl apt-transport-https ca-certificates sudo \  
&& curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \  
&& locale-gen en_US.UTF-8 \  
&& apt-get update && apt-get install -y nodejs \  
&& npm install -g grunt-cli  
RUN apt-get -y update && \  
apt-get install --force-yes -yq \  
wget \  
build-essential \  
sed \  
dpkg-dev \  
debhelper \  
createrepo \  
libcurl4-gnutls-dev \  
libglib2.0-dev \  
libgdk-pixbuf2.0-dev \  
libgtkglext1-dev \  
libatk1.0-dev \  
libcairo2-dev \  
libxml2-dev \  
libxss-dev \  
libgconf2-dev \  
default-jre \  
qt5-qmake \  
qt5-default \  
qtchooser \  
p7zip-full \  
git \  
subversion  
  
VOLUME /var/lib/onlyoffice  
  
CMD bash -C '/var/lib/onlyoffice/build.sh'  


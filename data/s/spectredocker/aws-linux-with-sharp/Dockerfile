FROM amazonlinux  
  
ADD nodesource.gpg.key /etc  
  
WORKDIR /tmp  
  
RUN yum -y install nasm python34 python34-setuptools libpng-devel zlib1g-dev
autoconf automake gcc libjpeg gifsicle wget libtool  
RUN easy_install-3.4 pip  
RUN wget
https://github.com/mozilla/mozjpeg/releases/download/v3.1/mozjpeg-3.1-release-
source.tar.gz && \  
tar xvfz mozjpeg-3.1-release-source.tar.gz && \  
cd mozjpeg && \  
./configure && \  
make && \  
make install  
  
RUN yum -y groupinstall "Development Tools" && \  
rpm --import /etc/nodesource.gpg.key && \  
curl --location --output ns.rpm
https://rpm.nodesource.com/pub_4.x/el/7/x86_64/nodejs-4.3.2-1nodesource.el7.centos.x86_64.rpm
&& \  
rpm --checksig ns.rpm && \  
rpm --install --force ns.rpm && \  
rm --force ns.rpm  
  
VOLUME /build  
  
WORKDIR /build


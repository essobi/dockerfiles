FROM centos:7  
MAINTAINER AttractGroup  
  
RUN yum update -y && yum clean all  
#RUN rpm -Uvhf http://mirrors.kernel.org/fedora-epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
RUN yum install -y yum-utils  
RUN yum-config-manager --enable cr  
RUN yum install -y epel-release  
RUN yum install -y \  
python-pip \  
python-setuptools \  
nginx \  
gcc \  
gcc-c++ \  
python-devel \  
unzip \  
wget \  
git \  
lapack-devel \  
supervisor \  
mysql-devel \  
mysql \  
rabbitmq-server \  
php-fpm \  
phpmyadmin \  
libjpeg-devel \  
make \  
flex \  
bison \  
gperf \  
ruby \  
openssl-devel \  
freetype-devel \  
fontconfig-devel \  
libicu-devel \  
libffi-devel \  
libxslt-devel \  
libxml2-devel \  
libxml++-devel \  
sqlite-devel \  
libpng-devel \  
cronie  
  
# needed to unpack phantomjs from tar.bz2  
RUN yum install -y bzip2  
  
#RUN git clone --recurse-submodules git://github.com/ariya/phantomjs.git  
#RUN /phantomjs/build.py  
#RUN mv /phantomjs/bin/phantomjs /usr/local/bin/  
#RUN rm -fr /phantomjs  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN tar -xvf phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/  
RUN rm -fr phantomjs-2.1.1-linux-x86_64  
RUN rm -fr phantomjs-2.1.1-linux-x86_64.tar.bz2  
  
RUN pip install uwsgi  
  
# install our code  
ADD ./req.txt /home/docker/code/req.txt  
  
# run pip install  
RUN pip install -r /home/docker/code/req.txt  
  
# Update yum cache, because in this image we do not run "yum update -y && yum
clean all"  
RUN yum makecache fast && yum install -y iproute


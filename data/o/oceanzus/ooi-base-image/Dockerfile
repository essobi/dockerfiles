# OOI UI Services  
# <https://github.com/asascience-open/ooi-ui-services>  
# Author: RPS ASA  
# Usage: <https://github.com/asascience-open/ooi-ui/wiki/Automated-
Deployment-(Docker)>  
FROM centos:centos6  
MAINTAINER The CentOS Project <cloud-ops@centos.org>  
  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release; yum clean all  
RUN yum -y install git; yum clean all  
RUN yum -y install sudo; yum clean all  
RUN yum -y install which; yum clean all  
RUN yum -y install mlocate; yum clean all  
RUN yum -y install bzip2; yum clean all  
RUN yum -y install bzip2-devel; yum clean all  
RUN yum -y install tar; yum clean all  
RUN yum -y update gmp; yum clean all  
RUN yum -y install wget; yum clean all  
  
RUN yum -y install gcc; yum clean all  
RUN yum -y install openssl-devel; yum clean all  
RUN yum -y install libxml2-devel; yum clean all  
RUN yum -y install libxslt-devel; yum clean all  
RUN yum -y install libcurl-devel; yum clean all  
RUN yum -y install sqlite-devel; yum clean all  
RUN yum -y install readline-devel; yum clean all  
RUN yum -y install db4-devel; yum clean all  
RUN yum -y install db4-devel-static; yum clean all  
  
RUN yum -y install ctags-etags; yum clean all  
RUN yum -y install tmux; yum clean all  
RUN yum -y install java-1.7.0-openjdk-devel; yum clean all  
RUN yum -y groupinstall 'Development Tools'; yum clean all  
RUN yum -y install zlib; yum clean all  
RUN yum -y install zlib-devel; yum clean all  
RUN yum -y install libpng; yum clean all  
RUN yum -y install libpng-devel; yum clean all  
RUN yum -y install libpng-static; yum clean all  
RUN yum -y install freetype; yum clean all  
RUN yum -y install freetype-devel; yum clean all  
  
# PostgreSQL Installation  
RUN yum -y install postgresql-devel  
WORKDIR /tmp  
RUN wget http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-
centos93-9.3-1.noarch.rpm  
RUN yum -y localinstall pgdg-centos93-9.3-1.noarch.rpm; yum clean all  
RUN yum -y install postgresql93 postgresql93-server postgresql93-libs
postgresql93-contrib postgresql93-devel; yum clean all  
RUN yum -y install postgis2_93; yum clean all  
RUN wget http://yum.postgresql.org/9.4/redhat/rhel-6-x86_64/pgdg-
centos94-9.4-1.noarch.rpm  
RUN yum -y localinstall pgdg-centos94-9.4-1.noarch.rpm  
  
# HDF5 Installation  
WORKDIR /tmp  
RUN wget
http://www.hdfgroup.org/ftp/HDF5/current/bin/RPMS/hdf5-1.8.14-1.with.szip.encoder.el6.x86_64.rpm  
RUN yum -y install hdf5-1.8.14-1.with.szip.encoder.el6.x86_64.rpm; yum clean
all  
RUN rm -rf hdf5-1.8.14-1.with.szip.encoder.el6.x86_64.rpm  
  
# NetCDF4 Installation  
WORKDIR /tmp  
RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.3.2.tar.gz  
RUN tar -zxvf netcdf-4.3.2.tar.gz -C /usr/local/src/  
RUN rm -rf netcdf-4.3.2.tar.gz  
WORKDIR /usr/local/src/netcdf-4.3.2  
RUN ./configure --prefix=/usr/local \--enable-netcdf-4 --enable-dap --enable-
shared && /usr/bin/make && /usr/bin/make install  
  
# Python Installation  
WORKDIR /tmp  
RUN wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tgz && tar -xzvf
Python-2.7.6.tgz -C /usr/local/src/  
RUN rm -rf Python-2.7.6.tgz  
WORKDIR /usr/local/src/Python-2.7.6  
RUN ./configure --with-zlib --prefix=/usr/local && /usr/bin/make &&
/usr/bin/make altinstall  
RUN ln -s /usr/local/bin/python2.7 /usr/local/bin/python27  
  
# Virutal Environment Installation  
WORKDIR /root  
RUN wget https://raw.githubusercontent.com/brainsik/virtualenv-
burrito/master/virtualenv-burrito.sh  
RUN chmod +x virtualenv-burrito.sh  
RUN ./virtualenv-burrito.sh  
WORKDIR /root  
RUN chmod +x /root/.venvburrito/startup.sh  
RUN source /root/.venvburrito/startup.sh && mkvirtualenv --no-site-packages
--python=/usr/local/bin/python27 ooiui  
RUN rm -rf virtualenv-burrito.sh  
  
# OOI UI Environment  
ENV WORKON_HOME /root/.virtualenvs  
  
  
  


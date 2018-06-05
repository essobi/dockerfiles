FROM centos:7  
MAINTAINER Yoshikazu Iikura <iikura@me.com>  
WORKDIR /app  
ENV PYTHONPATH '/app/Web-API:/app/Shared-Libraries/Python:/app/Data-
Export:/app/Data-Management:/app/Data-
Transform:/app/Analysis:/app/Reports:/app/Tests'  
ENV LD_LIBRARY_PATH "/usr/local/lib/:LD_LIBRARY_PATH"  
ENV ANSIBLE_CONNECTION local  
ENV GIT_SSL_NO_VERIFY true  
ADD *.txt /app/  
##################################  
# Install EPEL repo  
##################################  
RUN yum -y install epel-release \  
  
###################################  
# Installing gdal1.11, psycopg2, wget  
# gcc gcc-c++ python-devel make  
# python-lxml gdal gdal-devel  
# libxslt-devel libxml2-devel  
###################################  
  
&& yum install -y \  
make \  
gdal-python.x86_64 \  
opencv-python.x86_64 \  
python-psycopg2.x86_64 \  
wget \  
gcc \  
gcc-c++ \  
gcc-gfortran \  
libgfortran \  
python-devel \  
python-lxml \  
gdal \  
gdal-devel \  
libxslt-devel \  
libxml2-devel \  
python-reportlab \  
postgres*dev* \  
openssl* \  
nodejs \  
npm \  
bzip2 \  
git \  
sudo  
  
  
##################################  
# Adding get-pip.py,  
# libspatialindex & pipinstall.sh  
# Update Pip  
##################################  
  
RUN wget https://bootstrap.pypa.io/get-pip.py \  
&& mkdir /tmp/spatialindex \  
&& wget --directory-prefix=/tmp/spatialindex/
http://download.osgeo.org/libspatialindex/spatialindex-src-1.7.0.tar.gz \  
&& python get-pip.py  
  
  
##################################  
# Build SpatialIndex  
# Credit pvillard/agdc-docker  
#################################  
  
RUN tar -xvzf /tmp/spatialindex/spatialindex-src-1.7.0.tar.gz -C
/tmp/spatialindex \  
&& cd /tmp/spatialindex/spatialindex-src-1.7.0/ \  
&& ./configure; make; make install \  
&& echo export LD_LIBRARY_PATH=/usr/local/lib/ >> /root/.bashrc && source
/root/.bashrc \  
&& pip install -U Rtree && yum install -y which  
RUN echo hello \  
&& pip install -r /app/requirements.txt \  
&& pip install -r /app/requirements_linux.txt  
  
WORKDIR /  


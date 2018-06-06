FROM centos  
MAINTAINER Yoshikazu Iikura "iikura@me.com"  
# python and relevant tools  
RUN yum install -y \  
wget make gcc which \  
git gcc-gfortran libgfortran python-devel  
  
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py  
# for gdal and opencv  
RUN yum install -y opencv-python.x86_64  
  
RUN yum install -y epel-release && yum install -y gdal-python.x86_64 gdal
gdal-devel  
  
# pip python packages  
Run pip install \--upgrade pip numpy && pip install scipy pyproj fiona  
  


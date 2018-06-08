FROM centos:7  
MAINTAINER DrTrigon <dr.trigon@surfeu.ch>  
  
# LABEL author.user1="Abdeali JK <abdealikothari@gmail.com>" \  
# author.user2="DrTrigon <dr.trigon@surfeu.ch>"  
# Initial update  
RUN yum -y update  
  
# Enable Repos: EPEL, Nux desktop repo  
RUN yum install -y epel-release  
RUN rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro && \  
rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-
release-0-5.el7.nux.noarch.rpm  
  
# Basic packages  
RUN yum install -y \  
make \  
git  
  
# Pip - install latest version so that wheels are used  
RUN yum install -y python-pip && \  
pip install -U pip  
  
# libmagic  
RUN yum install -y file-devel file-libs  
  
# ExifTool  
RUN yum install -y perl-Image-ExifTool  
  
# OpenCV  
RUN yum install -y opencv-python  
  
# Image Magick / wand  
RUN yum install -y ImageMagick-devel python-devel  
  
# avprobe / ffprobe (From EPEL)  
RUN yum install -y ffmpeg  
  
# ZXing  
RUN yum install -y java  
  
# Dlib  
RUN yum install -y cmake boost-python python-devel boost boost-devel gcc-
gfortran gcc-c++ openblas-devel liblapack-devel  
  
# ZBar  
RUN yum install -y zbar-devel python-devel  
  
# Add the repository  
RUN git clone https://github.com/pywikibot-catfiles/file-metadata.git
/opt/file-metadata  
  
# Test requirements  
RUN pip install -r /opt/file-metadata/test-requirements.txt  
  
# Ugly hack to install zbar-devel. CentOS 7 doesn't have copr and can't
install  
# https://copr.fedorainfracloud.org/coprs/mmraka/epel7-addons/ easily. So  
# we just download the required packages for now...  
RUN yum install -y ImageMagick-c++ && \  
rpm -Uvh https://copr-
be.cloud.fedoraproject.org/results/mmraka/epel7-addons/epel-7-x86_64/zbar-0.10-15.fc19/zbar-0.10-15.el7.centos.x86_64.rpm
&& \  
rpm -Uvh https://copr-
be.cloud.fedoraproject.org/results/mmraka/epel7-addons/epel-7-x86_64/zbar-0.10-15.fc19/zbar-
devel-0.10-15.el7.centos.x86_64.rpm  
  
#RUN pip install pip==7.0.0  
RUN yum install -y libpng-devel  
RUN pip install -U cython  
  
# Install package  
RUN pip install /opt/file-metadata --upgrade  
RUN pip install -e /opt/file-metadata  


# Python 2.7 with Image Processing Libraries  
#  
# --- Image Stack ---  
# luzh/python2.7-imaging  
# luzh/python2.7-numerical  
# luzh/python2.7-baseline  
# luzh/centos7  
  
FROM luzh/python2.7-numerical  
  
# Refer to http://pillow.readthedocs.org/en/3.0.x/installation.html for Pillow
dependencies.  
  
RUN yum -y install libjpeg-turbo libjpeg-turbo-devel \  
&& yum -y install libpng libpng-devel \  
&& yum -y install libtiff libtiff-devel \  
&& yum -y install freetype freetype-devel \  
&& yum -y install openjpeg openjpeg-devel \  
&& yum -y install zlib zlib-devel \  
&& yum -y install libzip libzip-devel \  
&& yum -y install lcms2 lcms2-devel \  
&& yum -y install tcl tcl-devel \  
&& yum -y install tk tk-devel \  
&& yum -y install libwebp libwebp-devel \  
&& yum -y install ImageMagick \  
&& pip install --no-cache-dir Pillow matplotlib \  
&& yum clean all  


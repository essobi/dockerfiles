FROM centos:centos6  
  
# Enable EPEL for Node.js  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
  
RUN yum install -y npm wget tar gcc libpng libjpeg libpng-devel libjpeg-devel
ghostscript libtiff libtiff-devel freetype freetype-devel  
  
RUN wget
http://sourceforge.net/projects/graphicsmagick/files/graphicsmagick/1.3.21/GraphicsMagick-1.3.21.tar.gz
\  
&& tar zxvf GraphicsMagick-1.3.21.tar.gz \  
&& cd GraphicsMagick-1.3.21 \  
&& ./configure --enable-shared \  
&& make && make install  


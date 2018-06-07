FROM holmes/ghostscript:9.15  
MAINTAINER Holmes Team <holmes@holmesdoc.com>  
  
ENV GRAPHICKSMAGICK_VERSION 1.3.20  
RUN yum install -y gcc gcc-c++ make libpng libjpeg libpng-devel libjpeg-devel
giflib libtiff libtiff-devel freetype freetype-devel tar  
  
RUN DIR=$(mktemp -d) \  
&& cd ${DIR} \  
&& curl -L -Os
http://78.108.103.11/MIRROR/ftp/GraphicsMagick/1.3/GraphicsMagick-${GRAPHICKSMAGICK_VERSION}.tar.gz
\  
&& tar zxf GraphicsMagick-${GRAPHICKSMAGICK_VERSION}.tar.gz \  
&& cd GraphicsMagick-${GRAPHICKSMAGICK_VERSION} \  
&& ./configure --enable-shared \  
&& make \  
&& make install \  
&& make distclean \  
&& rm -rf ${DIR}  
  
ENTRYPOINT ["gm"]


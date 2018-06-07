FROM centos:centos7  
MAINTAINER Holmes Team <holmes@holmesdoc.com>  
  
ENV GHOSTSCRIPT_VERSION 9.15  
RUN yum install -y gcc gcc-c++ make libpng libjpeg libpng-devel libjpeg-devel
giflib libtiff libtiff-devel freetype freetype-devel tar  
  
RUN DIR=$(mktemp -d) \  
&& cd ${DIR} \  
&& curl -L -Os
http://downloads.ghostscript.com/public/ghostscript-${GHOSTSCRIPT_VERSION}.tar.gz
\  
&& tar zxf ghostscript-${GHOSTSCRIPT_VERSION}.tar.gz \  
&& cd ghostscript-${GHOSTSCRIPT_VERSION} \  
&& ./configure --prefix="$SRC" \--bindir="${SRC}/bin" \  
&& make \  
&& make install \  
&& make distclean \  
&& rm -rf ${DIR}  
  
ENTRYPOINT ["gs"]  
CMD ["--version"]


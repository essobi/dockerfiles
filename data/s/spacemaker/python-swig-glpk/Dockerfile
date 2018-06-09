FROM python:3.6.4-alpine3.7  
# Set required utility program versions  
ENV SWIG_VER 3.0.12  
ENV GLPK_VER 4.65  
ENV PYBUILDER_VER 0.11.12  
# Runtime Dependencies  
RUN apk update \  
&& apk add \  
ca-certificates \  
wget \  
pcre-dev \  
gmp \  
gfortran \  
freetype-dev \  
libpng-dev \  
openblas-dev \  
&& update-ca-certificates  
  
# Build Dependencies  
RUN apk add --no-cache --virtual \  
build-dependencies \  
build-base \  
g++ \  
make \  
autoconf  
  
# Make and install Swig  
RUN wget http://downloads.sourceforge.net/swig/swig-$SWIG_VER.tar.gz && \  
tar -xvzf swig-$SWIG_VER.tar.gz && cd swig-$SWIG_VER && \  
./configure --prefix=/usr && make && make install && cd .. && \  
rm -Rf swig-$SWIG_VER && rm swig-$SWIG_VER.tar.gz  
  
# Make and install GLPK  
RUN wget http://ftp.gnu.org/gnu/glpk/glpk-$GLPK_VER.tar.gz && \  
tar -xvzf glpk-$GLPK_VER.tar.gz && cd glpk-$GLPK_VER && \  
./configure --prefix=/usr && make && make check && \  
make install && make distclean && \  
cd .. && rm -Rf glpk-$GLPK_VER && rm glpk-$GLPK_VER.tar.gz  
  
# Install PyBuilder  
RUN pip install pybuilder==$PYBUILDER_VER  
  
CMD ["/bin/sh"]  
  


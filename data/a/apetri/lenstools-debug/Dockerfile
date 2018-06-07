FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install --no-install-recommends -y make \  
gcc \  
g++ \  
wget \  
tar \  
libgsl2 \  
libfftw3-3 \  
libfftw3-dev \  
libboost-all-dev \  
libffi-dev \  
python \  
python-dev \  
python-distribute \  
python-pip \  
scons \  
cmake \  
pkg-config \  
libgsl0-dev \  
gfortran \  
libblas-dev \  
liblapack-dev \  
python-scipy \  
git \  
libpng-dev \  
libfreetype6-dev  
  
RUN pip install wheel  
RUN pip install numpy  
  
# Install treecorr  
RUN pip install treecorr  
RUN pip install pyfits  
  
# Install galsim  
RUN pip install pyyaml  
RUN pip install starlink-pyast  
  
RUN mkdir build  
WORKDIR "/build"  
  
RUN wget https://github.com/rmjarvis/tmv/archive/v0.73.tar.gz  
RUN tar xf v0.73.tar.gz  
WORKDIR "/build/tmv-0.73"  
RUN scons && scons install  
  
WORKDIR "/build"  
RUN wget https://github.com/GalSim-developers/GalSim/archive/v1.4.1.tar.gz  
RUN tar xf v1.4.1.tar.gz  
WORKDIR "/build/GalSim-1.4.1"  
RUN scons && scons install  
  
# Install nicaea  
WORKDIR "/build"  
RUN wget http://www.cosmostat.org/wp-content/uploads/2014/12/nicaea_2.5.tgz  
RUN tar xf nicaea_2.5.tgz  
WORKDIR "/build/nicaea_2.5/build"  
RUN cmake .. && make && make install  
  
# Install lenstools  
RUN ln -s /usr/lib/x86_64-linux-gnu/libgsl.a /usr/lib/libgsl.a && \  
ln -s /usr/lib/x86_64-linux-gnu/libgslcblas.a /usr/lib/libgslcblas.a && \  
ln -s /usr/lib/x86_64-linux-gnu/libfftw3.a /usr/lib/libfftw3.a && \  
ln -s /usr/lib/x86_64-linux-gnu/libgsl.so /usr/lib/libgsl.so && \  
ln -s /usr/lib/x86_64-linux-gnu/libgslcblas.so /usr/lib/libgslcblas.so && \  
ln -s /usr/lib/x86_64-linux-gnu/libfftw3.so /usr/lib/libfftw3.so  
  
WORKDIR "/build"  
RUN wget https://github.com/apetri/LensTools/archive/0.6.tar.gz  
RUN tar xf 0.6.tar.gz  
WORKDIR "/build/LensTools-0.6"  
RUN sed -i 's\/usr/local\/usr\' setup.cfg && sed -i 's/False/True/' setup.cfg
&& sed -i '12s\/usr\/build/nicaea_2.5\' setup.cfg  
RUN python setup.py install


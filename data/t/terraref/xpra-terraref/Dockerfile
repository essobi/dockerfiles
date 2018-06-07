FROM ndslabs/xpra-base:1.0.9  
  
RUN yum update -q -y && \  
yum install -y \  
java-1.8.0-openjdk \  
openbox xorg-x11-apps \  
xterm \  
antlr \  
antlr-C++ \  
bison \  
make \  
automake \  
gcc \  
gcc-c++ \  
kernel-devel \  
flex \  
gdb \  
git \  
gsl-bin \  
gsl-devel \  
pax \  
vim \  
wget \  
netcdf \  
expat-devel \  
zlib-devel \  
numpy \  
scipy \  
matplotlib \  
libX11-devel \  
libXaw-devel \  
libpng-devel \  
netcdf4-python \  
python-devel \  
sqlite-devel \  
geos-devel \  
proj-devel \  
python-pip \  
PyQt4-web* \  
redhat-rpm-config && \  
CFLAGS=-I/usr/include pip install pyspatialite && \  
wget -O /etc/yum.repos.d/qgis-2-10-epel-7.repo
https://copr.fedoraproject.org/coprs/neteler/QGIS-2.10-Pisa/repo/epel-7/neteler-
QGIS-2.10-Pisa-epel-7.repo && \  
yum update -q -y && \  
yum install -y qgis qgis-grass qgis-python && \  
cd / && wget
https://www.giss.nasa.gov/tools/panoply/download/PanoplyJ-4.8.7.tgz && \  
tar xvfz PanoplyJ-4.8.7.tgz && \  
yum clean all  
  
RUN cd /usr/local/src && \  
wget ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-2.2.24.tar.gz && \  
gunzip -c udunits-2.2.24.tar.gz | pax -r && \  
cd udunits-2.2.24 && ./configure && make install && make clean  
  
RUN cd /usr/local/src && \  
wget
https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-1.10.0-patch1/src/hdf5-1.10.0-patch1.tar.gz
&& \  
tar xvfz hdf5-1.10.0-patch1.tar.gz && \  
cd hdf5-1.10.0-patch1 && ./configure --prefix=/usr/local && make install &&
make clean && \  
cd /usr/local/src  
  
RUN wget https://github.com/Unidata/netcdf-c/archive/v4.4.1.1.tar.gz -O
netcdf-v4.4.1.1.tar.gz && \  
tar xvfz netcdf-v4.4.1.1.tar.gz && \  
cd netcdf-c-4.4.1.1/ && ./configure --prefix=/usr/local/ && make install &&
make clean && \  
cd /usr/local/src  
  
RUN wget https://github.com/nco/nco/archive/4.6.6.tar.gz -O nco-4.6.6.tar.gz
&& \  
tar xvzf nco-4.6.6.tar.gz && cd nco-4.6.6/ && \  
./configure --enable-static --enable-shared --enable-udunits2 --disable-
udunits --enable-gsl --enable-ncoxx --enable-netcdf4 --enable-regex --disable-
dap && \  
make install && make clean  
  
RUN cd /usr/local/src && \  
wget ftp://cirrus.ucsd.edu/pub/ncview/ncview-2.1.7.tar.gz && \  
tar xvfz ncview-2.1.7.tar.gz && cd ncview-2.1.7/ && \  
./configure && make install && make clean  
  
  
ENV PATH /PanoplyJ:$PATH  
COPY entrypoint.sh /  
#COPY index.html /usr/share/xpra/www  
VOLUME /root  
EXPOSE 10000  
  
CMD [ "/entrypoint.sh"]  


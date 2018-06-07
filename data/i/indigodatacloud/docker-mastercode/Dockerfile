FROM fedora:23  
ENV sqlite_version="3100200"  
RUN dnf install -y \  
autoconf \  
automake \  
git \  
gcc \  
gcc-c++ \  
gcc-gfortran \  
libX11-devel \  
make \  
patch \  
rpm-build \  
tar \  
wget \  
which  
  
RUN dnf install -y \  
root \  
root-physics  
  
RUN dnf install -y \  
blas \  
blas-devel \  
lapack \  
lapack-devel  
  
RUN dnf install -y \  
texlive-tetex  
  
RUN dnf install -y \  
scipy \  
python3-Cython \  
python3-devel \  
python3-numpy \  
python3-matplotlib \  
python3-scipy \  
tkinter  
  
RUN dnf install -y Cython  
  
RUN dnf install --allowerasing -y python-matplotlib  
  
RUN wget https://www.sqlite.org/2016/sqlite-autoconf-${sqlite_version}.tar.gz
-O /tmp/sqlite-autoconf-${sqlite_version}.tar.gz && \  
tar xvfz /tmp/sqlite-autoconf-${sqlite_version}.tar.gz -C /tmp  
  
WORKDIR /tmp/sqlite-autoconf-${sqlite_version}  
RUN ./configure CFLAGS=-DSQLITE_MAX_VARIABLE_NUMBER=100000
--prefix=/usr/local/ && \  
make && \  
make install  
WORKDIR /  


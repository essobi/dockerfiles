FROM centos:6.6  
LABEL maintainer "tylern@jlab.org"  
ENV TERM xterm  
  
ENV ROOTSYS /usr/local/root  
ENV PATH $ROOTSYS/bin:$PATH  
ENV PYTHONDIR $PYTHONDIR:$ROOTSYS  
ENV LD_LIBRARY_PATH
$ROOTSYS/lib:$PYTHONDIR/lib:$ROOTSYS/bindings/pyroot:$LD_LIBRARY_PATH  
ENV DYLD_LIBRARY_PATH
/usr/lib:$ROOTSYS/lib:$PYTHONDIR/lib:$ROOTSYS/bindings/pyroot:$DYLD_LIBRARY_PATH  
ENV PYTHONPATH $PYTHONPATH:$ROOTSYS/lib:$ROOTSYS/bindings/pyroot  
  
RUN yum -y install epel-release \  
&& yum install -y \  
which mv wget xz tar file scons bzip2 \  
bash tcsh \  
git subversion \  
cmake make imake \  
gcc-c++ gcc gcc-gfortran \  
perl \  
xbae-devel \  
libXaw-devel \  
parallel \  
blas-devel \  
blas-static \  
lapack-devel \  
lapack-static \  
mysql-devel \  
python-devel \  
libjpeg-devel \  
libpng-devel \  
tcl \  
tcl-devel \  
tk \  
tk-devel \  
libtool \  
mlocate \  
openmotif-devel \  
#binutils \  
#libX11-devel \  
#libXpm-devel \  
#libXft-devel \  
#libXext-devel \  
#patch \  
#expat-devel \  
#bzip2-devel \  
#sqlite-devel \  
#openssl-devel \  
#pcre-devel \  
#mesa-libGL-devel \  
#mesa-libGLU-devel \  
#glew-devel \  
#ftgl-devel \  
#fftw-devel \  
#cfitsio-devel \  
#graphviz-devel \  
#avahi-compat-libdns_sd-devel \  
#libldap-dev \  
#libxml2-devel \  
#gsl-static \  
#slibXmu-devel \  
#libXp-devel \  
#libXt-devel \  
&& rm -rf /var/cache/* \  
&& ln -s /usr/lib64/liblapack.a /usr/lib64/liblapack3.a  
  
RUN cd /tmp/ \  
&& wget https://github.com/root-project/root/archive/v5-34-36.tar.gz \  
&& tar -xvf v5-34-36.tar.gz \  
&& rm -f v5-34-36.tar.gz \  
&& cd root-5-34-36/ \  
&& ./configure --all --disable-x11 --prefix=$ROOTSYS \  
&& make -j$(nproc) && make && make install \  
&& rm -rf /tmp/*  
  
COPY root-entrypoint.sh /usr/local/sbin  
  
ENTRYPOINT ["/usr/local/sbin/root-entrypoint.sh"]  


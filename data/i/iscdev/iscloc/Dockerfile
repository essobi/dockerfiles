FROM centos:centos7  
MAINTAINER Przemyslaw Ozgo <linux@ozgo.info>  
  
COPY compile-iscloc.sh /compile-iscloc.sh  
  
ENV SLBM_VERSION=3.0.4 \  
QETC=/usr/src/iscloc/etc/ \  
SLBMROOT=/usr/src/slbm/ \  
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$SLBMROOT/lib \  
RSTT_SUPPORT=false  
  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y \  
tar \  
wget \  
make \  
automake \  
gcc \  
gcc-c++ \  
postgresql \  
postgresql-devel \  
lapack-devel \  
lapack \  
blas \  
blas-devel \  
ncurses-devel && \  
wget -O /tmp/iscloc.tgz ftp://isc-
mirror.iris.washington.edu/pub/iscloc/ISCloc.tar.gz && \  
mkdir -p /usr/src/iscloc && \  
tar zxf /tmp/iscloc.tgz -C /usr/src/iscloc --strip-components=1 && rm -f
/tmp/iscloc.tgz && \  
wget -O /tmp/slbm.tgz
http://www.sandia.gov/rstt/downloads/SLBM_Root.${SLBM_VERSION}.Linux.tar.gz &&
\  
mkdir -p /usr/src/slbm && \  
tar zxf /tmp/slbm.tgz -C /usr/src/slbm --strip-components=1 && rm -f
/tmp/slbm.tgz && \  
cd /usr/src/slbm && make clean_objs && make geotess && make cc && make c &&
/usr/src/slbm/environment_variables.sh && \  
/compile-iscloc.sh && rm -f /compile-iscloc.sh && \  
yum remove -y wget make automake gcc gcc-c++ postgresql-devel lapack-devel
blas-devel ncurses-devel && \  
yum clean all  
  
COPY container-files /  
  
ENTRYPOINT ["/bootstrap.sh"]  


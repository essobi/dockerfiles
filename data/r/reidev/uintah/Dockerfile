FROM reidev/nimbix-ubuntu-desktop-xenial  
LABEL maintainer="markus@dynamitedigits.com"  
  
## Build Uintah  
# hypre pulls in openmpi  
RUN apt-get update \  
&& apt-get install -y subversion libhypre-dev petsc-dev libxml2-dev \  
zlib1g-dev liblapack-dev cmake libglew-dev libxmu-dev g++ gfortran \  
libboost-all-dev git libxrender-dev libxi-dev  
  
ARG UINTAH_REV=57399  
RUN svn co --username=anonymous --password='' \--revision $UINTAH_REV
https://gforge.sci.utah.edu/svn/uintah/trunk /usr/local/src/uintah  
  
RUN mkdir /usr/local/src/uintah/build  
WORKDIR /usr/local/src/uintah/build  
  
RUN ../src/configure --enable-optimize --enable-arches --with-boost=/usr
--enable-wasatch_3p --with-petsc=/usr/lib/petscdir/3.6.2/x86_64-linux-gnu-real
--with-mpi=built-in CC=mpicc CXX=mpic++ F77=mpif77 \  
&& make -j $(($(nproc) * 2)) \  
&& echo 'export PATH=/usr/local/src/uintah/build/StandAlone:$PATH' >>
/etc/skel/.bashrc  
  
## Install Visit  
# Install libpng15 (version does not exist on Ubuntu)  
RUN cd ~/ \  
&& curl -O -L
https://prdownloads.sourceforge.net/sourceforge/libpng/libpng15/1.5.30/libpng-1.5.30.tar.gz
\  
&& tar xzf libpng-1.5.30.tar.gz \  
&& cd libpng-1.5.30 \  
&& ./configure --prefix=/usr \  
&& make -j "$(nproc)" \  
&& make install \  
&& cd .. && rm -r libpng-1.5.30 && rm libpng-1.5.30.tar.gz  
  
# Install VisIt (use RHEL version because it includes the Uintah plugin)  
RUN curl -O -L
http://portal.nersc.gov/project/visit/releases/2.12.3/visit2_12_3.linux-x86_64-rhel7.tar.gz
\  
&& tar xzf visit2_12_3.linux-x86_64-rhel7.tar.gz -C /opt \  
&& echo 'export PATH=/opt/visit2_12_3.linux-x86_64/bin:$PATH' >>
/etc/skel/.bashrc \  
&& rm visit2_12_3.linux-x86_64-rhel7.tar.gz  
  
## Finalize image  
# Refresh files from /etc/skel  
RUN rm -rf /home/nimbix && /sbin/mkhomedir_helper nimbix  
  
USER nimbix  
  
WORKDIR /data  
  
EXPOSE 22 5901 443  


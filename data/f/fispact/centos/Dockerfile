FROM centos:7.4.1708  
MAINTAINER UKAEA <admin@fispact.ukaea.uk>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="CentOS docker image for FISPACT-II" \  
org.label-schema.url="http://fispact.ukaea.uk/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/fispact/docker_centos" \  
org.label-schema.vendor="UKAEA" \  
org.label-schema.version=$VERSION \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.schema-version="1.0"  
  
# some environment variables for regression testing  
# for centos 7 we use the same refences as centos 6  
ENV FISPACT_SYSTEM_TESTS_REF centos_6.9_gfortran_6_xsbinaries  
ENV PYTHONDONTWRITEBYTECODE 1.  
ENV PYTEST_VERBOSE line  
  
ENV RUN_SCRIPT ~/.bashrc  
  
WORKDIR /  
  
# Install additional packages  
RUN yum install -y wget which make gmake less doxygen rsync nano tar texi2html
texinfo xz git && \  
yum install -y libgcc gcc-c++ && \  
yum install -y gmp-devel mpfr-devel libmpc-devel openssl-devel && \  
yum install -y python-devel autoconf automake zlib-devel libpng-devel libjpeg-
devel bzip2 zip && \  
yum install -y gsl-devel lapack-devel freetype-devel && \  
yum -y update && \  
yum -y install yum-utils && \  
yum -y groupinstall development && \  
yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel
&& \  
yum install -y readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-
devel expat-devel && \  
# get gcc 6 from devtoolset  
yum install -y centos-release-scl && \  
yum install -y devtoolset-6 && \  
ln -sf /opt/rh/devtoolset-6/root/usr/bin/g++ /usr/bin/g++ && \  
ln -sf /opt/rh/devtoolset-6/root/usr/bin/gcc /usr/bin/gcc && \  
# remove old c++ to avoid conflicts  
rm -rf /usr/bin/c++ && \  
# cent os has old gfortran-4, rename this and sym link the new gfortran-6  
mv /usr/bin/gfortran /usr/bin/gfortran-4 && \  
ln -sf /opt/rh/devtoolset-6/root/usr/bin/gfortran /usr/bin/gfortran && \  
yum install -y ncurses-lib ncurses ncurses-base ncurses-static libquadmath &&
\  
# install cmake 3  
cd / && wget http://www.cmake.org/files/v3.0/cmake-3.0.0.tar.gz && \  
tar -xzvf cmake-3.0.0.tar.gz && cd cmake-3.0.0 && \  
./bootstrap && \  
export NCPUS=$(getconf _NPROCESSORS_ONLN) && \  
gmake -j${NCPUS} && \  
gmake install && \  
cd / && wget http://python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz && \  
tar xf Python-3.4.3.tar.xz && \  
cd /Python-3.4.3 && \  
./configure --prefix=/usr/local --enable-optimizations --enable-shared
LDFLAGS="-Wl,-rpath /usr/local/lib" && \  
make -j${NCPUS} && make altinstall && make install && \  
# pip3 packages  
pip3.4 install --upgrade pip && \  
pip3.4 install pytest pytest-xdist pypact numpy && \  
cd / && rm -rf cmake-3.0.0.tar.gz cmake-3.0.0 Python-3.4.3.tar.xz Python-3.4.3  
  
CMD /bin/bash $RUN_SCRIPT  


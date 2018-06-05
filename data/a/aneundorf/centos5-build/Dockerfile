FROM centos:5  
MAINTAINER alexander.neundorf@sharpreflections.com  
  
# This is a docker image building a Centos-5 complete development environment
from  
# scratch.  
# Since Centos5 is EOL since April 2017, yum needs to check the
"vault"-repositories  
# (copied from https://github.com/astj/docker-centos5-vault )  
COPY ./yum.repos.d/ /etc/yum.repos.d/  
# install a bunch of development packages  
RUN yum update -y && \  
yum install libidn libXext mc joe nano wget curl.x86_64 strace subversion sudo
man man-pages -y && \  
yum groupinstall "Development Tools" -y && \  
yum install libxml2-devel libjpeg-devel mesa-libGLU-devel freetype-devel
fontconfig-devel apr-devel apr-util-devel openssl-devel -y && \  
yum install libX11-devel libXext-devel libXrender-devel libXi-devel libXrandr-
devel libXinerama-devel libXv-devel libXcursor-devel libSM-devel -y  
  
  
# install cmake  
WORKDIR /opt  
RUN mkdir -p /tmp/dl && \  
wget -P /tmp/dl \--no-check-certificate
https://cmake.org/files/v3.6/cmake-3.6.3-Linux-x86_64.tar.gz && \  
wget -P /tmp/dl \--no-check-certificate
https://cmake.org/files/v3.1/cmake-3.1.3-Linux-x86_64.tar.gz && \  
tar -zxvf /tmp/dl/cmake-3.6.3-Linux-x86_64.tar.gz && \  
tar -zxvf /tmp/dl/cmake-3.1.3-Linux-x86_64.tar.gz && \  
rm /tmp/dl/*  
  
  
# build various packages  
RUN mkdir -p /tmp/src/  
# get a recent enough sqlite:  
WORKDIR /tmp/src  
RUN wget http://www.sqlite.org/2016/sqlite-autoconf-3150100.tar.gz && \  
tar -zxvf sqlite-autoconf-3150100.tar.gz  
  
# get Apache runtime  
WORKDIR /tmp/src  
RUN svn co http://svn.apache.org/repos/asf/apr/apr/branches/1.3.x apr-1.3 && \  
cd apr-1.3 && \  
./buildconf && \  
./configure \--prefix=/opt/apr-1.3 \--enable-shared \--disable-static && \  
make -j4 && \  
make install  
  
# get Apache apr-util  
WORKDIR /tmp/src  
RUN svn co http://svn.apache.org/repos/asf/apr/apr-util/branches/1.3.x apr-
util-1.3 && \  
cd apr-util-1.3 && \  
./buildconf \--with-apr=../apr-1.3 && \  
./configure \--prefix=/opt/apr-1.3 \--with-apr=../apr-1.3/ \--enable-shared
\--disable-static && \  
make -j4 && \  
make install  
  
# install scons, needed to build Serf  
WORKDIR /opt  
RUN mkdir -p /tmp/dl && \  
mkdir -p /opt/scons-2.3 && \  
wget -P /tmp/dl http://prdownloads.sourceforge.net/scons/scons-
local-2.3.0.tar.gz && \  
cd scons-2.3 && \  
tar -zxvf /tmp/dl/scons-local-2.3.0.tar.gz && \  
rm /tmp/dl/*  
  
  
# get Apache Serf (needed for https in svn)  
WORKDIR /tmp/src  
RUN wget \--no-check-certificate
https://www.apache.org/dist/serf/serf-1.3.9.tar.bz2 && \  
tar -jxvf serf-1.3.9.tar.bz2 && \  
cd serf-1.3.9 && \  
/opt/scons-2.3/scons.py PREFIX=/opt/serf-1.3.9 APR=/opt/apr-1.3
APU=/opt/apr-1.3 && \  
/opt/scons-2.3/scons.py install  
  
  
  
# build svn 1.7  
WORKDIR /tmp/src  
RUN wget http://archive.apache.org/dist/subversion/subversion-1.7.22.tar.gz &&
\  
tar -zxvf subversion-1.7.22.tar.gz && \  
mkdir /tmp/src/subversion-1.7.22/sqlite-amalgamation && \  
cp sqlite-autoconf-3150100/sqlite3.c /tmp/src/subversion-1.7.22/sqlite-
amalgamation/ && \  
cd subversion-1.7.22 && \  
./configure \--prefix=/opt/svn-1.7 \--without-berkeley-db \--without-apxs
\--without-swig \--with-ssl \--with-apr=/opt/apr-1.3/ \--with-apr-
util=/opt/apr-1.3/ && \  
nice make -j6 && \  
make install  
  
  
# build svn 1.8  
WORKDIR /tmp/src  
RUN wget http://archive.apache.org/dist/subversion/subversion-1.8.16.tar.gz &&
\  
tar -zxvf subversion-1.8.16.tar.gz && \  
cp -R sqlite-autoconf-3150100 subversion-1.8.16/sqlite-amalgamation && \  
cd subversion-1.8.16 && \  
./configure \--prefix=/opt/svn-1.8 \--without-berkeley-db \--without-apxs
\--without-swig \--with-ssl \--with-apr=/opt/apr-1.3/ \--with-apr-
util=/opt/apr-1.3/ \--with-serf=/opt/serf-1.3.9/ && \  
nice make -j4 && \  
make install && \  
mv /opt/svn-1.8/bin/svn /opt/svn-1.8/bin/svn18 && \  
echo $'#!/bin/bash \n LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/serf-1.3.9/lib/
/opt/svn-1.8/bin/svn18 $*' > /opt/svn-1.8/bin/svn && \  
chmod 755 /opt/svn-1.8/bin/svn  
# build git  
WORKDIR /tmp/src  
# wget from www.kernel.org failed with an ssl error. source packages in newer
distros are usually xz, which we can't unpack on centos5  
RUN wget
http://ftp5.gwdg.de/pub/linux/slackware/slackware-12.2/source/d/git/git-1.6.0.3.tar.bz2
&& \  
tar -jxvf git-1.6.0.3.tar.bz2 && \  
cd git-1.6.0.3 && \  
./configure \--prefix=/opt/git && \  
make -j4 && \  
make install  
  
  
# try to save some space  
#RUN rm -rf /tmp/src  
#RUN mkdir -p /tmp/src/  
# build gcc 4.9.4  
#WORKDIR /tmp/src  
#RUN echo "*** Building gcc..." && \  
# echo "*** Downloading gcc & friends..." && \  
# wget http://ftp.gwdg.de/pub/misc/gcc/releases/gcc-4.9.4/gcc-4.9.4.tar.gz &&
\  
# wget http://ftp.gwdg.de/pub/misc/gcc/infrastructure/gmp-4.3.2.tar.bz2 && \  
# wget http://ftp.gwdg.de/pub/misc/gcc/infrastructure/mpfr-2.4.2.tar.bz2 && \  
# wget http://ftp.gwdg.de/pub/misc/gcc/infrastructure/mpc-0.8.1.tar.gz && \  
# wget http://ftp.gwdg.de/pub/misc/gcc/infrastructure/isl-0.12.2.tar.bz2 && \  
# wget http://ftp.gwdg.de/pub/misc/gcc/infrastructure/cloog-0.18.1.tar.gz && \  
# tar -zxvf gcc-4.9.4.tar.gz && \  
# cd gcc-4.9.4 && \  
# tar -jxvf ../gmp-4.3.2.tar.bz2 && \  
# mv gmp-4.3.2 gmp && \  
# tar -jxvf ../mpfr-2.4.2.tar.bz2 && \  
# mv mpfr-2.4.2 mpfr && \  
# tar -zxvf ../mpc-0.8.1.tar.gz && \  
# mv mpc-0.8.1 mpc && \  
# tar -jxvf ../isl-0.12.2.tar.bz2 && \  
# mv isl-0.12.2/ isl && \  
# tar -zxvf ../cloog-0.18.1.tar.gz && \  
# mv cloog-0.18.1 cloog && \  
# mkdir build && \  
# cd build/ && \  
# echo "*** Configuring gcc..." && \  
# ../configure --prefix=/opt/gcc-4.9.4 --disable-multilib --enable-
languages=c,c++,fortran && \  
# make -j4 && \  
# make install  
# cleanup  
RUN rm -rf /tmp/src  


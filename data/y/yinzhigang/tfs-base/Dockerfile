#  
# TFS is a distributed file system developed by Taobao.com.  
#  
  
#FROM debian:jessie  
FROM centos:6  
  
MAINTAINER zhigang <yin@zhigang.net>  
  
#COPY sources.list.squeeze /etc/apt/sources.list  
#COPY sources.list.jessie /etc/apt/sources.list  
#COPY Centos-6.repo /etc/yum.repos.d/CentOS-Base.repo  
COPY epel-6.repo /etc/yum.repos.d/epel.repo  
#COPY mysql-community-6.repo /etc/yum.repos.d/mysql-community.repo  
  
#RUN apt-get update && apt-get install -y g++-4.3 gcc-4.1 make automake
libtool libreadline-dev zlib1g-dev uuid-dev libgoogle-perftools-dev subversion
libmysqlclient-dev  
RUN yum clean all  
RUN yum install -y gcc.x86_64 gcc-c++.x86_64 make.x86_64 automake.noarch
libtool.x86_64 readline-devel.x86_64 zlib-devel.x86_64 libuuid-devel.x86_64
gperftools-devel.x86_64 jemalloc-devel.x86_64 mysql-devel.x86_64 ncurses-
devel.x86_64 boost-devel.x86_64 json-c-devel.x86_64 curl.x86_64 libcurl-
devel.x86_64 snappy-devel.x86_64 subversion.x86_64 unzip.x86_64  
  
ENV TBLIB_ROOT /opt/tb-common-utils  
ENV TAIR_ROOT /opt/tair  
  
RUN \  
mkdir -p ${TBLIB_ROOT} && \  
mkdir -p /opt/taobao && \  
cd /opt/taobao && \  
#svn co -r 18 http://code.taobao.org/svn/tb-common-utils/trunk tb-common-utils
&& \  
svn export -r 22 http://code.taobao.org/svn/tb-common-utils/trunk tb-common-
utils && \  
sh tb-common-utils/build.sh && \  
rm -rf tb-common-utils && \  
svn export -r 3089 http://code.taobao.org/svn/tair/trunk/ tair && \  
cd tair && \  
sh bootstrap.sh && ./configure --prefix=${TAIR_ROOT} --with-release=yes && \  
make && make install && \  
cd /opt/taobao && rm -rf /opt/taobao/tair && \  
curl https://codeload.github.com/yinzhigang/tfs/zip/master > tfs.zip && \  
unzip tfs.zip && \  
#git clone https://github.com/yinzhigang/tfs.git /opt/taobao/tfs && \  
#svn co http://code.taobao.org/svn/tfs/tags/release-2.6.4/ tfs && \  
#svn co http://code.taobao.org/svn/tfs/tags/release-2.2.16/ tfs && \  
cd /opt/taobao/tfs-master && \  
sh build.sh init && ./configure --prefix=/opt/tfs --with-tair-
root=${TAIR_ROOT} --with-release=yes && \  
make && make install && \  
cd / && rm -rf /opt/taobao  
  


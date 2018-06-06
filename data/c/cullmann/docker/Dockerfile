# base is CentOS 6.x  
FROM centos:centos6  
  
# the maintainer  
MAINTAINER Christoph Cullmann <cullmann@kde.org>  
  
# update all installed stuff  
RUN yum update -y  
  
# install base devel system (needed for our development and the building of
all following packages)  
RUN yum install -y coreutils file bzip2 tar unzip xz zip genisoimage wget perl
ruby gcc gcc-c++ flex bison mc vim-enhanced apr-devel apr-util-devel zlib-
devel gettext perl-ExtUtils-MakeMaker  
  
# install subversion (including local sqlite)  
RUN cd /tmp && wget
http://mirror.dkd.de/apache/subversion/subversion-1.8.9.tar.bz2 && tar -xjf
subversion-1.8.9.tar.bz2 && cd subversion-1.8.9 && wget
http://www.sqlite.org/sqlite-amalgamation-3071501.zip && unzip sqlite-
amalgamation-3071501.zip && mv sqlite-amalgamation-3071501 sqlite-amalgamation
&& ./configure --prefix=/usr && make -j8 && make install && cd .. && rm -rf
subversion*  
  
# install git  
RUN cd /tmp && wget
https://www.kernel.org/pub/software/scm/git/git-2.0.1.tar.xz && tar -xJf
git-2.0.1.tar.xz && cd git-2.0.1 && ./configure --prefix=/usr && make -j8 &&
make install && cd .. && rm -rf git*  
  
# get and install gcc (with all dependencies)  
RUN cd /tmp && wget
ftp://ftp.gwdg.de/pub/misc/gcc/releases/gcc-4.9.0/gcc-4.9.0.tar.bz2 && tar
-xjf gcc-4.9.0.tar.bz2 && cd gcc-4.9.0 && ./contrib/download_prerequisites &&
mkdir build && cd build && ../configure --prefix=/usr --disable-multilib
--enable-languages=c,c++ && make -j8 && make install-strip && cd ../.. && rm
-rf gcc*  


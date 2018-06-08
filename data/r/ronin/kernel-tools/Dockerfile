FROM centos:centos7  
MAINTAINER Raghavendra Prabhu me@rdprabhu.com  
LABEL version="0.2" description="Linux kernel tools"  
  
RUN yum install -y automake gcc make libtool autoconf pkgconfig gettext git
libaio gcc-c++ libaio-devel  
  
RUN yum install -y http://epel.check-update.co.uk/7/x86_64/e/epel-
release-7-5.noarch.rpm  
  
RUN git clone \--depth=1
git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git  
  
WORKDIR /linux/tools/vm  
  
RUN sed -i -e 's/apikfs/api/' Makefile  
  
RUN make page-types slabinfo page_owner_sort  
  
RUN install page-types slabinfo page_owner_sort /usr/bin/  
  
WORKDIR /linux/tools/  
  
RUN yum install -y flex bison slang-devel elfutils-libelf-devel audit-libs-
devel numactl-devel xz-devel python-devel perl-ExtUtils-Embed libdwarf-devel
zlib-devel elfutils-devel binutils-devel  
  
RUN make prefix=/usr perf_install  
  
RUN yum remove -y libaio-devel slang-devel elfutils-libelf-devel audit-libs-
devel numactl-devel xz-devel python-devel libdwarf-devel zlib-devel elfutils-
devel binutils-devel  
  


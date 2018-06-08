FROM centos:centos7  
MAINTAINER Raghavendra Prabhu me@rdprabhu.com  
LABEL version="0.1" description="Tools for filesystem testing, benchmarking
and debugging"  
  
RUN yum install -y automake gcc make libtool autoconf pkgconfig gettext git
libaio gcc-c++ libaio libaio-devel kernel-headers  
  
RUN yum install -y http://epel.check-update.co.uk/7/x86_64/e/epel-
release-7-5.noarch.rpm  
  
RUN yum install -y fs_mark xfsprogs dbench  
  
RUN git clone \--depth=1 https://github.com/axboe/fio  
WORKDIR /fio  
RUN make -j4  
RUN make install  
  
RUN yum install -y blktrace btrfs-progs e2fsprogs perf  


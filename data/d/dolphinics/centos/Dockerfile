FROM centos:6  
MAINTAINER Dolphinics  
  
ENV GITVER=git-2.9.5  
RUN yum -y install make autoconf libtool gcc gcc-c++ glibc-devel glibc-
devel.i686 \  
libgcc libgcc.i686 rpm-build kernel kernel-devel which qt-devel \  
curl-devel expat-devel gettext-devel openssl-devel zlib-devel \  
perl-devel  
  
#Install git from source  
ADD https://www.kernel.org/pub/software/scm/git/$GITVER.tar.gz /  
RUN tar -xf $GITVER.tar.gz && make -C $GITVER prefix=/usr all install && rm
-rf $GITVER*  
  
#install fake uname  
COPY uname.sh /  
RUN /uname.sh --install $(ls /lib/modules/ | head -n 1)  


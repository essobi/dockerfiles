FROM centos:6  
MAINTAINER sken <sken [at] sken.biz>  
  
RUN yum -y update  
RUN yum -y install gcc gmake autoconf automake libtool flex bison gperf gawk
m4 make openssl-devel readline-devel tar  
RUN yum clean all  
  
WORKDIR /usr/local/src  
ADD http://sourceforge.net/projects/virtuoso/files/virtuoso/7.2.0/virtuoso-
opensource-7.2.0_p1.tar.gz/download /usr/local/src/virtuoso.tgz  
RUN tar xfz virtuoso.tgz  
  
WORKDIR /usr/local/src/virtuoso-opensource-7.2.0_p1  
RUN ./configure --prefix=/usr/local/ --with-readline  
RUN nice make  
RUN nice make install  
  
EXPOSE 8890  
WORKDIR /usr/local/var/lib/virtuoso/db/  
CMD virtuoso-t -df  


FROM centos:6  
MAINTAINER The U-TEST Team  
  
# A working C/C++ compiler for 32/64 bits binaries  
RUN yum install -y gcc-c++ glibc-devel libstdc++-devel libgcc  
RUN yum install -y glibc-devel.i686 libstdc++-devel.i686 libgcc.i686  
  
# GIT & CMAKE  
RUN yum install -y git cmake ant wget swig createrepo rpm-build  
  
# Some U-TEST dependancies  
RUN yum install -y postgresql postgresql-server postgresql-odbc unixODBC  
  
# Dependancies for U-TEST Externals  
RUN yum install -y python-twisted xerces-c-devel ncurses-libs libicu \  
bzip2-libs libzip openmpi mpich readline \  
python-libs libcap-ng unixODBC-devel libxml2-devel \  
python-devel sqlite-devel openssl-devel keyutils-libs-devel \  
libpcap-devel \  
cppunit-devel libzip-devel java-1.7.0-openjdk-devel  
RUN yum install -y xerces-c-devel.i686 ncurses-libs.i686 libicu.i686 \  
bzip2-libs.i686 libzip.i686 openmpi.i686 mpich.i686 \  
readline.i686 python-libs.i686 libcap-ng.i686 \  
unixODBC-devel.i686 libxml2-devel.i686 \  
python-devel.i686 sqlite-devel.i686 openssl-devel.i686 keyutils-libs-
devel.i686 \  
libpcap-devel.i686 \  
cppunit-devel.i686 libzip-devel.i686  
  
# Hackish way to install the 386 versions of the JVM libraries on the 64-bit
OS  
RUN cd /tmp \  
&& yum install -y yum-utils \  
&& linux32 yumdownloader java-1.7.0-openjdk \  
&& cd / \  
&& rpm2cpio /tmp/java-1.7.0-openjdk-*.i686.rpm | cpio -idmv *i386* \  
&& ln -s /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.*/jre/lib/i386
/usr/lib/jvm/jre/lib/i386 \  
&& rm -f /tmp/java-*.rpm  
  
RUN yum install -y inkscape doxygen && yum clean all  


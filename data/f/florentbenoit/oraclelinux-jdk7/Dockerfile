FROM unbc/oraclelinux6  
MAINTAINER Florent.Benoit "Florent.Benoit@serli.com"  
# Requirements from
http://docs.oracle.com/html/E25460_01/r2_fr_requirements.htm#sthref11  
# Linux x86-64, Oracle Linux 6 UL1+  
RUN yum install -y binutils.x86_64 compat-libcap1.x86_64 compat-
libstdc++-33.x86_64 compat-libstdc++-33.i686 gcc.x86_64 gcc-c++.x86_64
glibc.x86_64  
RUN yum install -y glibc.i686 glibc-devel.i686 libaio.x86_64 libaio-
devel.x86_64 libgcc.x86_64 libstdc++.x86_64 libstdc++.i686
libstdc++-devel.x86_64  
RUN yum install -y libXext.i686 libXtst.i686 openmotif.x86_64
openmotif22.x86_64 redhat-lsb-core.x86_64 sysstat.x86_64  
  
# Java Download location. Note the build number is in the URL.  
#
http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html  
ENV JAVA_MINOR_VERSION 71  
ENV JAVA_BUILD_NUMBER 14  
ENV JAVA_HOME /usr/java/jdk1.7.0_$JAVA_MINOR_VERSION  
ENV PATH JAVA_HOME/bin:$PATH  
  
# Install Java JDK without leaving behind temporary files  
RUN curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/7u$JAVA_MINOR_VERSION-b$JAVA_BUILD_NUMBER/jdk-7u$JAVA_MINOR_VERSION-
linux-x64.rpm > jdk-7u$JAVA_MINOR_VERSION-linux-x64.rpm && \  
rpm -ivh jdk-7u$JAVA_MINOR_VERSION-linux-x64.rpm && \  
rm jdk-7u$JAVA_MINOR_VERSION-linux-x64.rpm  
  


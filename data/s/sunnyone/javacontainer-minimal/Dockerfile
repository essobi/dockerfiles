# Dockerfile for javacontainer-minimal  
FROM busybox  
MAINTAINER Vadym S. Khondar <vadym@khondar.name>  
LABEL "description"="javacontainer-minimal is BusyBox based docker container
with minimal changes to make installed Java (JRE or JDK) run."  
  
# setup java installation parameters  
#ARG JAVA_DIST_TYPE="jdk"  
#ARG JAVA_VERSION_MAJOR  
#ARG JAVA_VERSION_MINOR  
#ARG JAVA_BUILD  
ENV JAVA_HOME_HOME="/usr/lib/jvm" \  
JAVA_DIST_TYPE=${JAVA_DIST_TYPE:-jdk} \  
JAVA_VERSION_MAJOR=${JAVA_VERSION_MAJOR:-8} \  
JAVA_VERSION_MINOR=${JAVA_VERSION_MINOR:-66} \  
JAVA_BUILD=${JAVA_BUILD:-17}  
ENV JAVA_VERSION=${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}  
ENV JAVA_PACKAGE_URL="http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}-b${JAVA_BUILD}/${JAVA_DIST_TYPE}-${JAVA_VERSION}-linux-x64.tar.gz"  
ENV
JAVA_HOME="$JAVA_HOME_HOME/${JAVA_DIST_TYPE}1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}"  
# download ssl_helper for wget to handle https  
ADD https://busybox.net/downloads/binaries/ssl_helper-x86_64 /bin/ssl_helper  
RUN chmod 755 /bin/ssl_helper  
  
# download and install dependencies  
RUN mkdir -p /usr/bin && ln -s /bin/env /usr/bin  
RUN mkdir -p /tmp/install  
WORKDIR "/tmp/install"  
  
ADD http://archive.ubuntu.com/ubuntu/pool/universe/b/bash/bash-
static_4.3-14ubuntu1_amd64.deb /tmp/install/  
RUN ar x *.deb && \  
cd / && tar xJf /tmp/install/data.tar.xz && \  
ln -s /bin/bash-static /bin/bash && \  
rm -f /tmp/install/*  
  
ADD
http://archive.ubuntu.com/ubuntu/pool/main/g/gcc-5/gcc-5-base_5.2.1-22ubuntu2_amd64.deb
/tmp/install/  
RUN ar x *.deb && \  
cd / && tar xJf /tmp/install/data.tar.xz && \  
rm -f /tmp/install/*  
  
ADD
http://archive.ubuntu.com/ubuntu/pool/main/g/gcc-5/libgcc1_5.2.1-22ubuntu2_amd64.deb
/tmp/install/  
RUN ar x *.deb && \  
cd / && tar xJf /tmp/install/data.tar.xz && \  
rm -f /tmp/install/*  
  
ADD
http://archive.ubuntu.com/ubuntu/pool/main/g/glibc/libc6_2.21-0ubuntu4_amd64.deb
/tmp/install/  
RUN ar x *.deb && \  
cd / && tar xzf /tmp/install/data.tar.gz && \  
rm -f /tmp/install/*  
  
# download, unpack and register Oracle Java  
RUN mkdir -p $JAVA_HOME_HOME  
WORKDIR "$JAVA_HOME_HOME"  
  
RUN wget --no-check-certificate --header 'Cookie: oraclelicense=a'
$JAVA_PACKAGE_URL && \  
tar xzf ${JAVA_DIST_TYPE}-${JAVA_VERSION}-linux-x64.tar.gz && \  
ln -s $JAVA_HOME/bin/java /bin && \  
rm ${JAVA_DIST_TYPE}-${JAVA_VERSION}-linux-x64.tar.gz  
# end  


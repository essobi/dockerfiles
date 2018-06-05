FROM axeclbr/debian  
  
MAINTAINER axeclbr <axeclbr@posteo.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV JDK_MAJOR_VERSION="8"  
ENV JDK_MINOR_VERSION="102"  
ENV JDK_VERSION="${JDK_MAJOR_VERSION}u${JDK_MINOR_VERSION}"  
ENV JDK_BUILD="b14"  
ENV JDK_DIR="jdk1.${JDK_MAJOR_VERSION}.0_${JDK_MINOR_VERSION}"  
# Install Java.  
RUN apt-get update && apt-get install -y \  
wget \  
&& wget \  
\--no-check-certificate \  
\--no-cookies \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JDK_VERSION}-${JDK_BUILD}/jdk-${JDK_VERSION}-linux-x64.tar.gz \  
\--directory-prefix=/opt/ \  
&& cd /opt \  
&& tar xvzf jdk-${JDK_VERSION}-linux-x64.tar.gz \  
&& rm jdk-${JDK_VERSION}-linux-x64.tar.gz \  
&& ln -s /opt/${JDK_DIR}/bin/java /usr/local/bin/java \  
&& ln -s /opt/${JDK_DIR}/bin/javac /usr/local/bin/javac \  
&& apt-get remove -y wget \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /opt/${JDK_DIR}  
  
CMD ["/bin/bash"]  
  


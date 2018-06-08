FROM sergeyzh/centos6-epel  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com & Andrey Sizov,
andrey.sizov@jetbrains.com  
  
RUN yum clean all && rpm --rebuilddb && yum update -y && yum install -y unzip  
  
ENV JAVA_VER=1.8.0_91 JAVA_DWL_VER=8u91 JAVA_DWL_BVER=b14 \  
JAVA_HOME=/usr/java64/current  
ENV JDK_HOME=${JAVA_HOME} \  
PATH=${JAVA_HOME}/bin:${PATH}  
  
RUN mkdir /usr/java64 ; cd /usr/java64/ ; \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_DWL_VER}-${JAVA_DWL_BVER}/jdk-${JAVA_DWL_VER}-linux-x64.tar.gz
&& \  
cd /usr/java64/ && tar -xzf jdk-${JAVA_DWL_VER}-linux-x64.tar.gz && rm
jdk-${JAVA_DWL_VER}-linux-x64.tar.gz && \  
cd /usr/java64/ && ln -s jdk${JAVA_VER} current && \  
chown -R root:root /usr/java64 && \  
chmod -R a+rwX /usr/java64  
  
CMD /bin/bash  
  


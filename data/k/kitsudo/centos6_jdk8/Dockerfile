FROM kitsudo/aliyun_centos6.6  
MAINTAINER Dave Luo <kitsudo163@163.com>  
  
ENV JAVA_HOME=/opt/jdk8  
  
RUN yum install -y \  
tar  
RUN mkdir -p ${JAVA_HOME} && curl -sSL --header "Cookie: oraclelicense=accept-
securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.tar.gz | \  
tar zxv -C ${JAVA_HOME} \--strip-components 1  
  
ENV PATH=${JAVA_HOME}/bin:$PATH  
  
RUN alternatives --install "/usr/bin/java" "java" "${JAVA_HOME}/bin/java" 1  


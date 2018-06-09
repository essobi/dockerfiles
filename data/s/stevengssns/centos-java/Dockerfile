FROM centos:centos7  
  
MAINTAINER stevengssns <stevengssns@gmail.com>  
  
RUN curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u40-b25/jre-8u40-linux-x64.rpm >
jre-8u40-linux-x64.rpm && \  
yum -y \--nogpgcheck localinstall jre-8u40-linux-x64.rpm && \  
rm -f jre-8u40-linux-x64.rpm && \  
touch /etc/profile.d/java.sh && \  
echo '#!/bin/bash' >> /etc/profile.d/java.sh && \  
echo 'JAVA_HOME=/usr/java/jre1.8.0_40/' >> /etc/profile.d/java.sh && \  
echo 'PATH=$JAVA_HOME/bin:$PATH' >> /etc/profile.d/java.sh && \  
echo 'export PATH JAVA_HOME' >> /etc/profile.d/java.sh && \  
echo 'export CLASSPATH=.' >> /etc/profile.d/java.sh && \  
chmod +x /etc/profile.d/java.sh && \  
source /etc/profile.d/java.sh  
  
# Define default command.  
CMD ["java"]  


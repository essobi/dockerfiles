FROM oraclelinux:7-slim  
  
ENV JAVA_RPM jdk-linux-x64.rpm  
  
RUN curl -s -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/jdk-8u152-linux-x64.rpm
> $JAVA_RPM \  
&& yum -y install $JAVA_RPM \  
&& rm $JAVA_RPM  
  
ENV JAVA_HOME /usr/java/default


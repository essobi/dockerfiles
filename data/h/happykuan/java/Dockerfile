FROM happykuan/centos  
MAINTAINER "zhangzhikuan" <happykuan@yeah.net>  
  
#install JAVA  
ENV JAVA_HOME=/usr/local/jdk1.7.0_79 M2_HOME=/usr/local/apache-maven-3.3.9  
#download jdk  
RUN wget --no-check-certificate --no-cookie --header "Cookie:
oraclelicense=accept-securebackup-cookie;" http://download.oracle.com/otn-
pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz -O
/tmp/jdk-7u79-linux-x64.tar.gz && tar -zxvf /tmp/jdk-7u79-linux-x64.tar.gz -C
/usr/local/ && rm -f /tmp/jdk-7u79-linux-x64.tar.gz \  
&& wget http://mirrors.cnnic.cn/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz -O /tmp/apache-maven-3.3.9-bin.tar.gz && tar -zxvf
/tmp/apache-maven-3.3.9-bin.tar.gz -C /usr/local/ && rm -f /tmp/apache-
maven-3.3.9-bin.tar.gz \  
&& chown -R root:root $JAVA_HOME $M2_HOME  
  
  
#set PATH  
ENV PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH  
  
##########################################################  
RUN sed -i "146 a<mirror>\n \  
<id>ui</id>\n \  
<mirrorOf>central</mirrorOf>\n \  
<name>Human Readable Name for this Mirror.</name>\n \  
<url>http://uk.maven.org/maven2/</url>\n \  
</mirror>" $M2_HOME/conf/settings.xml  
##########################################################  
  
CMD ["/bin/bash"]  


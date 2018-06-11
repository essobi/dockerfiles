FROM valus/base  
  
MAINTAINER KOSUKE IIDA<iida@valus.co.jp>  
  
ENV HOME=/root  
ENV USER=root  
  
RUN curl --silent \--location https://rpm.nodesource.com/setup_5.x | bash - &&
\  
yum -y update && \  
yum -y install wget fontconfig-devel bzip2 unzip nodejs gcc-c++ make && \  
wget \  
\--no-check-certificate \  
\--no-cookies \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie"
"http://download.oracle.com/otn-pub/java/jdk/8u91-b14/jdk-8u91-linux-x64.rpm"
&& \  
yum -y localinstall jdk-8u91-linux-x64.rpm && \  
yum clean all && \  
rm jdk-8u91-linux-x64.rpm && \  
echo 'export JAVA_HOME="/usr/java/default"' >> /etc/profile.d/java.sh && \  
echo 'export PATH="${JAVA_HOME}/bin:${PATH}"' >> /etc/profile.d/java.sh && \  
echo 'export CLASSPATH=.' >> /etc/profile.d/java.sh && \  
source /etc/profile.d/java.sh && \  
cd /usr/local/lib/ && \  
wget
http://ftp.tsukuba.wide.ad.jp/software/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz && \  
tar zxvf apache-maven-3.3.9-bin.tar.gz && \  
ln -s apache-maven-3.3.9/ maven && \  
echo 'export M3_HOME="/usr/local/lib/maven"' >> /etc/profile.d/maven.sh && \  
echo 'export PATH="${M3_HOME}/bin:${PATH}"' >> /etc/profile.d/maven.sh && \  
source /etc/profile.d/maven.sh  


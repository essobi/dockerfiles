FROM debian:jessie  
  
MAINTAINER Rui Tang <tangrui.cn@gmail.com>  
  
ENV JAVA_6_HOME=/usr/lib/jvm/jdk-6-oracle-x64 \  
JAVA_7_HOME=/usr/lib/jvm/jdk-8-oracle-x64 \  
JAVA_8_HOME=/usr/lib/jvm/jdk-8-oracle-x64 \  
JAVA_HOME=/usr/lib/jvm/jdk-8-oracle-x64 \  
PINPOINT_VERSION=1.5.2  
###  
# 1. Packages java-package and fakeroot are used to convert JDK bin installer  
# into deb installer  
# 2. Packages libgl1-mesa-glx, libgtk2.0-0, libxslt1.1, libxtst6,  
# libxxf86vm1, libxt6 are required for make-jpkg  
###  
RUN echo 'deb http://httpredir.debian.org/debian/ jessie contrib' >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y wget git fakeroot java-package && \  
apt-get install -y libgl1-mesa-glx libgtk2.0-0 libxslt1.1 libxtst6 libxxf86vm1
libxt6 && \  
useradd pinpoint -m && \  
cd /home/pinpoint && \  
wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/6u45-b06/jdk-6u45-linux-x64.bin &&
\  
chown pinpoint:pinpoint jdk-6u45-linux-x64.bin && \  
su pinpoint -c 'yes | fakeroot make-jpkg jdk-6u45-linux-x64.bin' && \  
dpkg -i oracle-java6-jdk_6u45_amd64.deb && \  
rm jdk-6u45-linux-x64.bin && \  
rm oracle-java6-jdk_6u45_amd64.deb && \  
wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u91-b14/jdk-8u91-linux-x64.tar.gz
&& \  
[ $(md5sum jdk-8u91-linux-x64.tar.gz | grep --only-matching -m 1 '^[0-9a-f]*')
= 3f3d7d0cd70bfe0feab382ed4b0e45c0 ] && \  
chown pinpoint:pinpoint jdk-8u91-linux-x64.tar.gz && \  
su pinpoint -c 'yes | fakeroot make-jpkg jdk-8u91-linux-x64.tar.gz' && \  
dpkg -i oracle-java8-jdk_8u91_amd64.deb && \  
rm jdk-8u91-linux-x64.tar.gz && \  
rm oracle-java8-jdk_8u91_amd64.deb && \  
mkdir -p /usr/local/maven && \  
cd /usr/local/maven && \  
wget https://archive.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-
maven-3.2.5-bin.tar.gz && \  
wget https://archive.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-
maven-3.2.5-bin.tar.gz.md5 && \  
[ $(md5sum apache-maven-3.2.5-bin.tar.gz | grep --only-matching -m 1
'^[0-9a-f]*') = $(cat apache-maven-3.2.5-bin.tar.gz.md5) ] && \  
gpg --keyserver pgp.mit.edu --recv-key BB617866 && \  
wget https://archive.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-
maven-3.2.5-bin.tar.gz.asc && \  
gpg --verify apache-maven-3.2.5-bin.tar.gz.asc apache-maven-3.2.5-bin.tar.gz
&& \  
tar -xvzf apache-maven-3.2.5-bin.tar.gz --strip-components=1 && \  
rm apache-maven-3.2.5-bin.tar.gz && \  
rm apache-maven-3.2.5-bin.tar.gz.md5 && \  
rm apache-maven-3.2.5-bin.tar.gz.asc && \  
git clone https://github.com/naver/pinpoint.git /pinpoint && \  
cd /pinpoint && \  
git checkout tags/$PINPOINT_VERSION && \  
apt-get purge -y fakeroot java-package && \  
apt-get autoremove -y  
  
ENV PATH=$PATH:/usr/local/maven/bin  
WORKDIR /pinpoint  
VOLUME ["/pinpoint", "/root/.m2"]  
CMD ["mvn", "install", "-Dmaven.test.skip=true"]  


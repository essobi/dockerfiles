from centos:centos6  
  
ENV JAVA_VER 7u71  
ENV JAVA_VER_BUILD b14  
ENV ANT_VER 1.9.4  
ENV MAVEN_VER 3.2.2  
# Install EPEL and a few dependencies  
RUN rpm -Uvh --force http://mirrors.kernel.org/fedora-epel/6/x86_64/epel-
release-6-8.noarch.rpm; yum -y update; yum -y install git install subversion
unzip wget  
  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VER-$JAVA_VER_BUILD/jdk-$JAVA_VER-linux-x64.rpm" -O
jdk-7-linux-x64.rpm; rpm -Uvh jdk-7-linux-x64.rpm; rm -f jdk-7-linux-x64.rpm  
  
RUN wget http://archive.apache.org/dist/ant/binaries/apache-ant-$ANT_VER-
bin.zip; unzip apache-ant-$ANT_VER-bin.zip; mv apache-ant-$ANT_VER/ /opt/ant;
ln -s /opt/ant/bin/ant /usr/bin/ant; rm -rf apache-ant-$ANT_VER-bin.zip  
  
RUN wget http://archive.apache.org/dist/maven/binaries/apache-
maven-$MAVEN_VER-bin.zip; unzip apache-maven-$MAVEN_VER-bin.zip; mv apache-
maven-$MAVEN_VER/ /opt/maven; ln -s /opt/maven/bin/mvn /usr/bin/mvn; rm -rf
apache-maven-$MAVEN_VER-bin.zip  
  
ADD ./centos-base.sh /etc/profile.d/centos-base.sh  


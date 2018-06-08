FROM mimacom/centos7  
MAINTAINER sysadmin@mimacom.com  
  
ENV VERSION 7  
ENV UPDATE 80  
ENV BUILD 15  
ENV SIG none  
  
LABEL Description="CentOS 7 with Java JDK ${VERSION}u${UPDATE}-b${BUILD} from
oracle"  
  
# download java  
RUN yum update -y && \  
rm -rf /var/cache/yum/* && \  
yum install -y wget && \  
mkdir -p /opt/java && \  
wget --no-cookies https://nexus3.mimacom.com/repository/3rd-party/oracle-
java/jdk-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz -O /opt/jdk.tar.gz && \  
tar xfv /opt/jdk.tar.gz -C /opt/java/ --strip-components=1 && \  
rm -f /opt/jdk.tar.gz  
  
# add java to PATH  
COPY java_oraclejdk.sh /etc/profile.d/java.sh  


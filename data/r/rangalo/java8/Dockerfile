FROM rangalo/ubuntu:latest  
  
MAINTAINER rangalo "hard.mehta@gmail.com"  
  
RUN mkdir -p /opt/oracle && \  
wget -q \--no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2Ftechnetwork%2Fjava%2Fjavase%2Fdownloads%2Fjdk8-downloads-2133151.html;
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u101-b13/jdk-8u101-linux-x64.tar.gz && \  
mv -v jdk-8u101-linux-x64.tar.gz /opt/oracle && \  
cd /opt/oracle && tar zxf jdk-8u101-linux-x64.tar.gz && \  
cd /opt/oracle/ && rm -vf jdk-8u101-linux-x64.tar.gz && \  
ln -svn /opt/oracle/jdk1.8.0_101 /opt/oracle/jdk && \  
echo "JAVA_HOME=/opt/oracle/jdk" >> /etc/environment  
  
ENV JAVA_HOME /opt/oracle/jdk  
ENV PATH $JAVA_HOME/bin:$PATH  


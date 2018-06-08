FROM mirkosertic/centosbase  
MAINTAINER Mirko Sertic <mirko.sertic@web.de>  
  
# Install Oracle JDK  
RUN mkdir /opt/Oracle_Java && \  
cd /opt/Oracle_Java && \  
wget --header="Cookie:s_cc=true; s_nr=1412060362634;
gpw_e24=http%3A%2F%2Fwww.oracle.com%2Ftechnetwork%2Fjava%2Fjavase%2Fdownloads%2Fjdk7-downloads-1880260.html;
s_sq=%5B%5BB%5D%5D; notice_preferences=2:cb8350a2759273dccf1e483791e6f8fd;
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/7u67-b01/jdk-7u67-linux-x64.tar.gz && \  
tar xfz jdk-7u67-linux-x64.tar.gz && \  
chmod -R 755 /opt/Oracle_Java && \  
rm /opt/Oracle_Java/jdk-7u67-linux-x64.tar.gz && \  
ln -s /opt/Oracle_Java/jdk1.7.0_67 /opt/Oracle_Java/current_jdk && \  
update-alternatives --install "/usr/bin/java" "java"
"/opt/Oracle_Java/current_jdk/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javac" "javac"
"/opt/Oracle_Java/current_jdk/bin/javac" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"/opt/Oracle_Java/current_jdk/bin/javaws" 1 && \  
update-alternatives --install "/usr/bin/jar" "jar"
"/opt/Oracle_Java/current_jdk/bin/jar" 1 && \  
rm -rf /tmp/*  


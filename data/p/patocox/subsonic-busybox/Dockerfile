FROM progrium/busybox  
  
MAINTAINER patocox  
  
RUN opkg-install curl tar  
RUN mkdir java && \  
cd java && \  
curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" -O
http://download.oracle.com/otn-pub/java/jdk/7u75-b13/jre-7u75-linux-x64.tar.gz
&& \  
tar zvxf jre-7u75-linux-x64.tar.gz && \  
rm -rf jre-7u75-linux-x64.tar.gz  
  
RUN mkdir -p /var/subsonic/standalone && \  
cd /var/subsonic/standalone && \  
wget
http://downloads.sourceforge.net/project/subsonic/subsonic/5.2.1/subsonic-5.2.1-standalone.tar.gz
&& \  
tar zvxf subsonic-5.2.1-standalone.tar.gz && \  
rm -rf subsonic-5.2.1-standalone.tar.gz  
  
ADD subsonic.sh /var/subsonic/standalone/subsonic.sh  
WORKDIR /var/subsonic/standalone  
RUN chmod +x subsonic.sh  
  
CMD ./subsonic.sh  


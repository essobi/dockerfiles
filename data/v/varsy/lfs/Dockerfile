FROM sergeyzh/centos6-java  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
ENV LFS_VERSION=4.4.2 \  
LFS_XMS=512 \  
LFS_XMX=1024 \  
JAVA_HOME=/usr/java64/current \  
PATH=$PATH:$JAVA_HOME/bin  
  
RUN wget -q -O /root/lfs.${LFS_VERSION}.linux.x86-64.tar.gz
http://www.moonlit-
software.com/logfaces/downloads/lfs.${LFS_VERSION}.linux.x86-64.tar.gz && \  
tar zxf /root/lfs.${LFS_VERSION}.linux.x86-64.tar.gz -C /root/ && \  
rm -rf /root/lfs.${LFS_VERSION}.linux.x86-64.tar.gz && \  
sed -i '1 a JAVA_HOME=/usr/java64/current' /root/logFacesServer/bin/lfs && \  
sed -i '2 a APP_BIN=/root/logFacesServer/bin' /root/logFacesServer/bin/lfs &&
\  
sed -i 's/WRAPPER_CMD=\"\\./WRAPPER_CMD=\"\$\\{APP_BIN\\}/'
/root/logFacesServer/bin/lfs && \  
sed -i 's/WRAPPER_CONF=\"\\./WRAPPER_CONF=\"\$\\{APP_BIN\\}/'
/root/logFacesServer/bin/lfs  
  
ADD run-services.sh /  
RUN chmod +x /run-services.sh  
CMD /run-services.sh  
  
EXPOSE 8050 55200 1468 55201 514 55202 55203 55204 55205  


FROM mcreations/openwrt-java:8  
MAINTAINER Yousef Irman <irman@m-creations.net>  
  
ENV SYMMETRICDS_MAJOR_VERSION 3.8  
ENV SYMMETRICDS_MINOR_VERSION 16  
ENV SYMMETRICDS_VERSION
${SYMMETRICDS_MAJOR_VERSION}.${SYMMETRICDS_MINOR_VERSION}  
  
ENV SYMMETRICDS_HOME /opt/symmetric-ds  
  
  
  
ADD image/root /  
  
RUN opkg update && \  
opkg install unzip && \  
mkdir -p ${SYMMETRICDS_HOME} && \  
wget --progress=dot:giga
http://sourceforge.net/projects/symmetricds/files/symmetricds/symmetricds-${SYMMETRICDS_MAJOR_VERSION}/symmetric-
server-${SYMMETRICDS_MAJOR_VERSION}.${SYMMETRICDS_MINOR_VERSION}.zip/download
-O symmetric-server-${SYMMETRICDS_VERSION}.zip && \  
unzip symmetric-server-${SYMMETRICDS_VERSION}.zip && \  
cp -r symmetric-server-${SYMMETRICDS_VERSION}/* ${SYMMETRICDS_HOME}/ && \  
rm -rf symmetric-server-${SYMMETRICDS_VERSION}*  
  
CMD ["/start-symmertic-ds"]  


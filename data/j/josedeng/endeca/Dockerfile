FROM josedeng/jdk:jdk-1.7.0_80  
  
ADD wget.sh /tmp/wget.sh  
ADD tools.rsp /installer/tools.rsp  
ADD start.sh /start.sh  
  
RUN dos2unix /tmp/wget.sh && \  
dos2unix /installer/tools.rsp && \  
dos2unix /start.sh && \  
chmod a+x /start.sh && \  
apt-get update && \  
apt-get install -y wget unzip libaio1 && \  
source /tmp/wget.sh && \  
mv /tmp/V78226-01.zip /installer/platform.zip && \  
mv /tmp/V78211-01.zip /installer/mdex.zip && \  
mv /tmp/V78229-01.zip /installer/tools.zip && \  
mv /tmp/V78204-01.zip /installer/cas.zip && \  
chmod a+x -R /installer && \  
apt-get clean && \  
apt-get autoremove wget --purge -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
VOLUME ["/opt/endeca"]  
EXPOSE 8006 8888 8500 15000-16999  
ENTRYPOINT ["/start.sh"]  


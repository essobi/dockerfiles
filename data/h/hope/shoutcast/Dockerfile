FROM hope/centos  
  
ENV \  
SHOUTCAST_VERSION 2.5.1  
RUN \  
yum -y install wget && \  
  
# Install  
wget -P /tmp/
http://download.nullsoft.com/shoutcast/tools/sc_serv2_linux_x64-latest.tar.gz
&& \  
mkdir /usr/local/shoutcast && \  
tar -xzf /tmp/sc_serv2_linux_x64-latest.tar.gz -C /usr/local/shoutcast && \  
  
# Cleanup  
rm -f /tmp/sc_serv2_linux_x64-latest.tar.gz && \  
yum -y remove wget && \  
yum clean all  
  
ONBUILD COPY rootfs/ /  
  
EXPOSE 7777  
EXPOSE 7778  
WORKDIR /usr/local/shoutcast  
  
ENTRYPOINT ["./sc_serv"]  
CMD ["./sc.conf"]  


FROM ubuntu:16.04  
  
ENV PATH $PATH:/opt/dell/srvadmin/sbin:/opt/dell/srvadmin/bin  
  
RUN apt update && \  
apt -y dist-upgrade && \  
apt install -y apt-transport-https && \  
echo "deb https://linux.dell.com/repo/community/ubuntu xenial openmanage" |
tee -a /etc/apt/sources.list.d/linux.dell.com.sources.list && \  
gpg --keyserver pool.sks-keyservers.net --recv-key 1285491434D8786F && \  
gpg -a \--export 1285491434D8786F | apt-key add \- && \  
apt update && \  
apt install -y srvadmin-base srvadmin-storageservices kmod && \  
apt clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 161/udp 1311/tcp  
  
CMD srvadmin-services.sh restart && tail -f
/opt/dell/srvadmin/var/log/openmanage/dcsys64.xml  


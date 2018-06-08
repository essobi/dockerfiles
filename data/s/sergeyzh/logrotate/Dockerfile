FROM sergeyzh/centos6-epel  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
ADD rpms/ /root/rpms/  
RUN yum localinstall -y /root/rpms/*.rpm  
  
ADD etcd-v0.4.5-linux-amd64.tar.gz /  
RUN cd /etcd-v0.4.5-linux-amd64 ; mv etcdctl /usr/bin/ ; rm -rf
/etcd-v0.4.5-linux-amd64  
  
ADD run-services.sh /  
RUN chmod +x /run-services.sh ; mkdir -p /conf/logrotate  
  
CMD /run-services.sh  


FROM varsy/centos6-utils  
  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
ADD rpms/ /root/rpms/  
RUN yum localinstall -y /root/rpms/*.rpm || true  
  
ADD etcd-v0.4.5-linux-amd64.tar.gz /  
RUN cd /etcd-v0.4.5-linux-amd64 ; mv etcdctl /usr/bin/ ; rm -rf
/etcd-v0.4.5-linux-amd64  
  
ADD reloader.sh /  
RUN chmod a+x /reloader.sh  
  
ADD functions.sh /  
  
ADD run-services.sh /  
RUN chmod +x /run-services.sh ; mkdir -p /conf/nginx  
  
CMD /run-services.sh  
  
EXPOSE 80 443  


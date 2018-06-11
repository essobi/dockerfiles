FROM sergeyzh/centos6-epel  
  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
RUN yum install -y nrpe rsyslog  
  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network  
  
ADD etcd-v0.4.5-linux-amd64.tar.gz /  
RUN cd /etcd-v0.4.5-linux-amd64 ; mv etcdctl /usr/bin/ ; rm -rf
/etcd-v0.4.5-linux-amd64  
  
ADD reloader.sh /  
RUN chmod a+x /reloader.sh  
  
ADD run-services.sh /  
RUN chmod a+x /run-services.sh  
CMD /run-services.sh  
  
EXPOSE 5666  


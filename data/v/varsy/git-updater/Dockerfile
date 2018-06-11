FROM sergeyzh/centos6-epel  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com; Andrey Sizov,
andrey.sizov@jetbrains.com  
  
RUN cp -f /usr/share/zoneinfo/Europe/Moscow /etc/localtime  
  
RUN yum install -y git  
  
ADD update-git-repo.sh /  
ADD reloader.sh /  
  
RUN ln -s /sshconfig /root/.ssh  
  
ADD etcd-v0.4.5-linux-amd64.tar.gz /  
RUN cd /etcd-v0.4.5-linux-amd64 ; mv etcdctl /usr/bin/ ; rm -rf
/etcd-v0.4.5-linux-amd64  
  
ADD run-services.sh /  
RUN chmod +x /run-services.sh /update-git-repo.sh /reloader.sh  
  
CMD /run-services.sh


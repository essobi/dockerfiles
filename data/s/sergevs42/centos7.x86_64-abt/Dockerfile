FROM centos:7  
MAINTAINER Serge at abrikus@gmail.com  
  
RUN yum -y --setopt=tsflags=nodocs install
https://github.com/sergevs/abt/releases/download/3.1.2/abt-3.1.2-ssv1.el7.noarch.rpm
&& \  
yum -y --setopt=tsflags=nodocs install
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \  
yum -y --setopt=tsflags=nodocs install iproute hostname nfs-utils rpcbind && \  
yum clean all && \  
rm -f /etc/yum.repos.d/*Sources.repo && \  
echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
RUN sed -i -e 's/el7.centos/el7/' /etc/rpm/macros.dist  
COPY .rpmmacros /root/  
COPY user.init /usr/bin/  
  
ENTRYPOINT ["/usr/bin/user.init"]  


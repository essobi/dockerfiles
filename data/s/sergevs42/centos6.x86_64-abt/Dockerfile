FROM centos:6.9  
MAINTAINER Serge at abrikus@gmail.com  
  
RUN yum -y --setopt=tsflags=nodocs install
https://github.com/sergevs/abt/releases/download/3.1.2/abt-3.1.2-ssv1.el6.noarch.rpm
&& \  
yum -y --setopt=tsflags=nodocs install
https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm && \  
yum -y --setopt=tsflags=nodocs install iproute hostname nfs-utils rpcbind
openssh-clients && \  
yum -y --setopt=tsflags=nodocs install
https://packages.endpoint.com/rhel/6/os/x86_64/git-1.8.4-1.ep.x86_64.rpm
https://packages.endpoint.com/rhel/6/os/x86_64/perl-Git-1.8.4-1.ep.noarch.rpm
&& \  
yum clean all && \  
echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
COPY .rpmmacros /root/  
COPY user.init /usr/bin/  
  
ENTRYPOINT ["/usr/bin/user.init"]  


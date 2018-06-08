FROM goldeneggg/centos:7  
MAINTAINER goldeneggg  
  
# install packages  
RUN yum -y install wget epel-release tcp_wrappers gnutls  
  
# install ngircd  
RUN wget -O libevent.rpm
ftp://ftp.pbone.net/mirror/download.fedora.redhat.com/pub/fedora/linux/releases/20/Everything/x86_64/os/Packages/l/libident-0.32-9.fc20.x86_64.rpm  
RUN rpm -ivh libevent.rpm  
RUN wget -O ngircd.rpm
ftp://ftp.pbone.net/mirror/download.fedora.redhat.com/pub/fedora/linux/development/21/x86_64/os/Packages/n/ngircd-21.1-5.fc21.x86_64.rpm  
RUN rpm -ivh ngircd.rpm  
RUN yum clean all  
ADD ADD_FILES/etc/ngircd.conf /etc/ngircd.conf  
  
# expose port 6667  
EXPOSE 6667  
# service ngircd  
# if you execute "docker run" without arguments, run ngircd on foreground  
ENTRYPOINT ["/usr/sbin/ngircd"]  
CMD ["-n"]  


from centos:latest  
RUN yum groupinstall -y 'Development Tools' && yum -y install
https://dl.fedoraproject.org/pub/epel/7/x86_64/i/inotify-
tools-3.14-8.el7.x86_64.rpm && yum clean all  
  
COPY watch.sh /  
LABEL RUN='docker run -d -v /tmp/centos/rpms:/rpms:rw,Z IMAGE sh /watch.sh'  


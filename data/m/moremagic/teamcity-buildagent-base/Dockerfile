FROM centos  
MAINTAINER moremagic <itoumagic@gmail.com>  
RUN yum -y update  
RUN yum install -y passwd openssh-server openssh-clients initscripts  
RUN yum install -y install git wget curl tar zip unzip expect sshpass && yum
-y update  
  
RUN yum install -y libgcc_s.so.1 ld-linux.so.2  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/7u80-b15/jdk-7u80-linux-i586.rpm  
RUN rpm -Uvh jdk-7u80-linux-i586.rpm  
  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u65-b17/jdk-8u65-linux-i586.rpm  
RUN rpm -Uvh jdk-8u65-linux-i586.rpm  
  
RUN echo 'root:root' | chpasswd  
RUN /usr/sbin/sshd-keygen  
  
EXPOSE 22 9090  
CMD /usr/sbin/sshd -D  


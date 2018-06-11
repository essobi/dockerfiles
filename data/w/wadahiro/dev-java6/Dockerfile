FROM wadahiro/centos-jp:6.8  
LABEL maintainer "Hiroyuki Wada <wadahiro@gmail.com>"  
  
RUN curl https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-
maven.repo > /etc/yum.repos.d/epel-apache-maven.repo  
RUN yum install -y java-1.6.0-openjdk java-1.6.0-openjdk-devel && yum install
-y --enablerepo=*debug* java-1.6.0-openjdk-debuginfo && yum install -y apache-
maven-3.2.5 && yum install -y git zip unzip patch && yum clean all  
  
CMD "/bin/bash"  


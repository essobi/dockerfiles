FROM centos:7  
MAINTAINER krytin <krytin.vitaly@apriorit.com>  
  
RUN yum -y update && yum clean all  
RUN yum groupinstall -y 'Development Tools'  
  
RUN yum install -y clang clang-devel llvm-devel cmake3 cmake python-testtools
python-pip wget  
  
RUN yum install -y
https://rpmfind.net/linux/centos/7.4.1708/updates/x86_64/Packages/kernel-3.10.0-693.2.2.el7.x86_64.rpm  
RUN yum install -y
https://rpmfind.net/linux/centos/7.4.1708/updates/x86_64/Packages/kernel-3.10.0-693.21.1.el7.x86_64.rpm  
RUN yum install -y
https://rpmfind.net/linux/centos/7.4.1708/updates/x86_64/Packages/kernel-
devel-3.10.0-693.2.2.el7.x86_64.rpm  
RUN yum install -y
https://rpmfind.net/linux/centos/7.4.1708/updates/x86_64/Packages/kernel-
devel-3.10.0-693.21.1.el7.x86_64.rpm  
  
#*******************************************  


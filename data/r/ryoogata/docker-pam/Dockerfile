FROM chef/centos-6  
MAINTAINER ryoogata  
  
ADD Centos-Source.repo /etc/yum.repos.d/Centos-Source.repo  
  
RUN yum install -y tar bzip2 yum-utils rpm-build whici wget sudo which  
  
RUN yum-builddep -y pam  
RUN yumdownloader --source pam  
RUN rpmbuild --rebuild --define 'WITH_AUDIT 0' \--define 'dist +noaudit'
pam*.src.rpm  
RUN rpm -Uvh --oldpackage ~/rpmbuild/RPMS/*/pam*+noaudit*.rpm  


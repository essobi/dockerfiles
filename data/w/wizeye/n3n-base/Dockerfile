FROM centos:7  
# Run upgrades  
RUN yum -y update; yum clean all  
  
# Install basic packages  
RUN yum -y install wget net-tools perl yum-utils epel-release; yum clean all  
  
# Install nodejs  
RUN wget --ftp-user=innowatch --ftp-password=inno0529^!
ftp://wizeye.publish.n3n.co.kr/wizeye/nodejs/4.x/nodejs-4.7.0-1nodesource.el7.centos.x86_64.rpm  
RUN rpm -Uvh nodejs-4.7.0-1nodesource.el7.centos.x86_64.rpm  
  
# Install mono  
RUN rpm --import
"http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"  
RUN yum-config-manager --add-repo http://download.mono-
project.com/repo/centos/  
RUN yum -y install mono-complete-4.2.1.102 monodevelop; yum clean all  
  
CMD ["/bin/bash"


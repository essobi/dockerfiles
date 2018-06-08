FROM sawarame/centos  
  
RUN cd /tmp/ && wget
http://dev.mysql.com/get/Downloads/MySQL-5.6/MySQL-5.6.19-1.linux_glibc2.5.x86_64.rpm-
bundle.tar  
RUN cd /tmp/ && tar xvf MySQL-5.6.19-1.linux_glibc2.5.x86_64.rpm-bundle.tar  
RUN cd /tmp/ && rpm -ivh MySQL-shared-
compat-5.6.19-1.linux_glibc2.5.x86_64.rpm  
RUN cd /tmp/ && rpm -ivh MySQL-shared-5.6.19-1.linux_glibc2.5.x86_64.rpm  
RUN cd /tmp/ && rpm -ivh MySQL-devel-5.6.19-1.linux_glibc2.5.x86_64.rpm  
RUN cd /tmp/ && rpm -ivh MySQL-client-5.6.19-1.linux_glibc2.5.x86_64.rpm  
RUN cd /tmp/ && rpm -ivh MySQL-server-5.6.19-1.linux_glibc2.5.x86_64.rpm  
RUN cd /tmp/ && rpm -ivh MySQL-embedded-5.6.19-1.linux_glibc2.5.x86_64.rpm


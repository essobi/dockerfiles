FROM centos:7  
  
# Base install up-to-date and epel is required for many packages  
RUN yum update -y && \  
yum install -y epel-release && \  
# Software development tools, RPM build requirements  
yum install -y auto{conf,make} ctags elfutils gcc{,-c++} gettext intltool
libtool make patch{,utils} && \  
yum install -y redhat-rpm-config rpm-{build,sign} spectool && \  
yum install -y git yum-utils && \  
yum clean all && \  
curl -o /usr/local/bin/tar2rpm
https://raw.githubusercontent.com/linuxlefty/tar2rpm/master/tar2rpm.sh && \  
chmod +x /usr/local/bin/tar2rpm  
  
RUN mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS,SPECS}  
  
CMD ["bash"]  


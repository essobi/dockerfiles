FROM centos:5.11  
LABEL maintainer "Bezeklik"  
  
RUN sed -i -e '/mirrorlist=h/d' -e '/#baseurl/ s/^#//' -e
's/$releasever/5.11/' -e 's|mirror.centos.org/centos|vault.centos.org|'
/etc/yum.repos.d/CentOS-Base.repo && \  
sed -i -e '/mirrorlist=h/d' -e '/#baseurl/ s/^#//' -e 's/$releasever/5.11/' -e
's|mirror.centos.org/centos|vault.centos.org|' /etc/yum.repos.d/CentOS-
fasttrack.repo && \  
sed -i -e '/mirrorlist=h/d' -e '/#baseurl/ s/^#//' -e 's/$releasever/5.11/' -e
's|mirror.centos.org/centos|vault.centos.org|'
/etc/yum.repos.d/libselinux.repo && \  
yum clean all && yum -y update  
  
EXPOSE 80  
  
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]  


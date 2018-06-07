FROM kalledk/centos:7  
MAINTAINER Kalle R. Møller  
  
RUN yum install -y http://pkgs.repoforge.org/rpmforge-release/rpmforge-
release-0.5.3-1.el7.rf.x86_64.rpm \  
&& yum install -y \  
createrepo \  
mkisofs \  
xorriso \  
python-requests \  
&& yum clean all -y  
  
ADD files /docker-files  
  
VOLUME ["/data", "/iso", "/buildcache"]  
  
ENTRYPOINT ["/docker-files/entry.sh"]  


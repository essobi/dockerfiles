FROM centos  
MAINTAINER Dave Johnston email: dave.johnston@icloud.com  
WORKDIR /tmp  
  
# Install Additional Repos  
#  
RUN yum install -y http://pkgs.repoforge.org/rpmforge-release/rpmforge-
release-0.5.3-1.el6.rf.x86_64.rpm  
  
# Install Apache and other tools  
#  
RUN yum install -y httpd \  
createrepo \  
xorriso \  
wget \  
&& yum clean all  
  
# Fetch the CentOS ISO and update the repo  
#  
RUN mkdir -p /var/www/html/centos/6.5 \  
&& wget
http://mirror.simwood.com/centos/6.5/isos/x86_64/CentOS-6.5-x86_64-minimal.iso
\  
&& osirrox -indev /tmp/CentOS-6.5-x86_64-minimal.iso -extract /Packages
/var/www/html/centos/6.5/ \  
&& pushd /var/www/html/centos/ \  
&& createrepo . \  
&& popd \  
&& rm CentOS-6.5-x86_64-minimal.iso \  
&& rm /etc/httpd/conf.d/welcome.conf  
  
EXPOSE 80  
ENTRYPOINT [ "/usr/sbin/httpd" ]  
CMD [ "-D", "FOREGROUND" ]  


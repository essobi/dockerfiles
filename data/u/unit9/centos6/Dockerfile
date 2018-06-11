FROM centos:6  
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>  
# Loosely based on existing base image for Debian  
# Uses similar concepts  
# Upgrade base system  
RUN yum upgrade -y && yum clean all  
  
# Install runit  
RUN curl -s -o /tmp/script.rpm.sh \  
https://packagecloud.io/install/repositories/imeyer/runit/script.rpm.sh \  
&& sha256sum /tmp/script.rpm.sh \  
&& bash /tmp/script.rpm.sh \  
&& rm /tmp/script.rpm.sh \  
&& yum install -y runit \  
&& yum clean all  
  
# Install init  
RUN curl -fsSL -o /tmp/runsvinit.tgz \  
https://github.com/peterbourgon/runsvinit/releases/download/v2.0.0/runsvinit-
linux-amd64.tgz \  
&& sha256sum /tmp/runsvinit.tgz \  
&& cd /sbin \  
&& tar zxf /tmp/runsvinit.tgz \  
&& chown root:root /sbin/runsvinit \  
&& rm /tmp/runsvinit.tgz  
  
# Boot scripts  
COPY rc.init rc.local /etc/  
CMD ["/etc/rc.init"]  


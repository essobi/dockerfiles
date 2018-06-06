FROM centos:7  
MAINTAINER Stefan Schueffler <s.schueffler@softgarden.de>  
  
RUN rpm --import http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7
\  
&& yum -y install epel-release \  
&& yum -y update \  
&& yum -y install bind-utils clamav clamav-data-empty clamav-scanner gpg rsync
unzip which wget \  
&& yum clean all  
  
ENV CUS_VERSION=5.6.2  
RUN set -x \  
&& curl -L https://github.com/extremeshok/clamav-unofficial-
sigs/archive/$CUS_VERSION.tar.gz | tar -xz \  
&& cd clamav-unofficial-sigs-$CUS_VERSION \  
&& mkdir -p /usr/local/bin/ \  
&& mkdir -p /var/log/clamav-unofficial-sigs/ \  
&& mkdir -p /etc/clamav-unofficial-sigs/ \  
&& cp -f clamav-unofficial-sigs.sh /usr/local/bin/clamav-unofficial-sigs.sh \  
&& chmod +x /usr/local/bin/clamav-unofficial-sigs.sh \  
&& cp -f config/os.centos7.conf /etc/clamav-unofficial-sigs/os.conf \  
&& cp -f config/master.conf /etc/clamav-unofficial-sigs/ \  
&& rm -rf clamav-unofficial-sigs-$CUS_VERSION  
  
# add default user conf  
ADD user.conf /etc/clamav-unofficial-sigs/user.conf  
  
ADD entrypoint.sh /  
  
VOLUME ["/var/lib/clamav", "/var/lib/clamav-unofficial-sigs"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD []  


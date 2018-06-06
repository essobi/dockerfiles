FROM centos:7  
MAINTAINER Stefan Schueffler <s.schueffler@softgarden.de>  
  
RUN rpm --import http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7
\  
&& yum -y install epel-release \  
&& yum -y update \  
&& yum -y install clamav-data-empty clamav-update \  
&& yum clean all  
  
RUN set -x \  
&& sed -ri ' \  
s/Example/#Example/g; \  
s/#LogTime yes/LogTime yes/g; \  
s/#Checks 24/Checks 48/g; \  
s/#Foreground yes/Foreground yes/g; \  
s!#NotifyClamd /path/to/clamd.conf!NotifyClamd /etc/clamd.conf!g; \  
' /etc/freshclam.conf \  
\  
&& { \  
echo 'TCPSocket 3310'; \  
echo 'TCPAddr clamd'; \  
} | tee /etc/clamd.conf  
  
VOLUME ["/var/lib/clamav"]  
  
ENTRYPOINT ["freshclam"]  
CMD ["-d"]  


FROM fedora:21  
MAINTAINER Benoît Vidis <contact@benoitvidis.com>  
  
RUN yum install -y \  
atk \  
avahi-devel \  
bzr \  
cups \  
cups-devel \  
cups-libs \  
curl \  
gcc \  
git \  
glibc \  
glibc-2.20-8.fc21.i686 \  
go \  
gtk2 \  
gtk2-2.24.28-1.fc21.i686 \  
libglade2 \  
libglade2-2.6.4-12.fc21.i686 \  
libstdc++ \  
libstdc++-4.9.2-6.fc21.i686 \  
pango \  
pango-1.36.8-6.fc21.i686 \  
pangox-compat \  
popt-1.16-5.fc21.i686 \  
tar \  
|| true \  
&& yum clean all \  
&& cd /root \  
&& curl -SLO
http://gdlp01.c-wss.com/gds/6/0100004596/04/Linux_CAPT_PrinterDriver_V270_uk_EN.tar.gz
\  
&& tar xvf Linux_CAPT_PrinterDriver_V270_uk_EN.tar.gz \  
&& rpm --rebuilddb \  
&& rpm -ivh Linux_CAPT_PrinterDriver_V270_uk_EN/64-bit_Driver/RPM/cndrvcups-
common-3.20-1.x86_64.rpm \  
&& rpm -ivh Linux_CAPT_PrinterDriver_V270_uk_EN/64-bit_Driver/RPM/cndrvcups-
capt-2.70-1.x86_64.rpm \  
&& mkdir -p /var/log/CCPD \  
&& export GOPATH=/root \  
&& go get github.com/google/cloud-print-connector/... \  
&& echo done  
  
COPY etc/cups/cupsd.conf /etc/cups/  
COPY etc/ccpd.conf /etc/  
COPY killproc /usr/local/bin/  
COPY docker-entrypoint.sh /  
  
CMD ["/docker-entrypoint.sh"]  
  


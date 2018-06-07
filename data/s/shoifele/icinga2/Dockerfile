# shoifele/icinga2  
FROM shoifele/bone  
MAINTAINER Sebastian Sauer <info@dynpages.de>  
MAINTAINER Christoph Wiechert <wio@psitrax.de>  
  
  
RUN wget -q -O - http://packages.icinga.org/icinga.key | apt-key add - && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
icinga2 \  
icinga2-ido-mysql \  
mysql-client \  
openssh-server \  
monitoring-plugins-basic && \  
chsh -s /bin/bash nagios && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /build  
  
ADD rootfs /  
  
EXPOSE 22  
VOLUME ["/etc/icinga2", "/run/icinga2/cmd"]  
  
CMD ["/init"]  


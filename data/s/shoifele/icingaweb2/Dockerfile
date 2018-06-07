# shoifele/icingaweb2  
FROM shoifele/nginx-php5  
  
MAINTAINER Sebastian Sauer <info@dynpages.de>  
MAINTAINER Christoph Wiechert <wio@psitrax.de>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends openssh-client && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /build  
  
# --branch v2.0.0-rc1  
# lets use 20.0.0 MASTER instead :)  
RUN git clone git://git.icinga.org/icingaweb2.git /temp/icingaweb2-git 2>&1 &&
\  
rm -rf /temp/icingaweb2-git/.git  
  
ADD rootfs /  
  
VOLUME [ "/etc/icingaweb2"]  


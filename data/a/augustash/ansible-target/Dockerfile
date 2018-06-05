FROM augustash/baseimage:1.0.0  
MAINTAINER Pete McWilliams <pmcwilliams@augustash.com>  
  
ARG DEBIAN_FRONTEND="noninteractive"  
# environment  
ENV APTLIST \  
openssh-server \  
python \  
sudo  
  
# packages & configure  
RUN apt-get -yqq update && \  
apt-get -yqq install --no-install-recommends --no-install-suggests $APTLIST
$BUILD_DEPS && \  
  
sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config &&
\  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \  
sed -ri 's/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g'
/etc/ssh/sshd_config && \  
mkdir -p /root/.ssh/ && \  
  
apt-get -yqq purge --auto-remove -o APT::AutoRemove::RecommendsImportant=false
$BUILD_DEPS && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# root filesystem  
COPY rootfs /  
  
# run s6 supervisor  
ENTRYPOINT ["/init"]  
EXPOSE 22  


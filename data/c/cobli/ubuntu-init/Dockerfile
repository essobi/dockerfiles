FROM ubuntu-upstart:14.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN printf '#!/bin/sh\nexit 101\n' > /usr/sbin/policy-rc.d; chmod +x
/usr/sbin/policy-rc.d  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
openssh-server sudo dbus curl iproute2 net-tools git-core vim && \  
rm -rf /var/lib/apt/lists/*  
  
RUN useradd -s /bin/bash -m -d /home/test test  
RUN printf "Defaults !requiretty\ntest ALL=(ALL) NOPASSWD: ALL" >
/etc/sudoers.d/test  
  
EXPOSE 22  
ENTRYPOINT ["/sbin/init"]  


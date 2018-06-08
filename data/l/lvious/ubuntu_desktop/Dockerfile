#  
# Ubuntu Desktop (Gnome) Dockerfile  
#  
# https://github.com/Lvious/Docker-Ubuntu-Desktop-Gnome  
#  
# Install GNOME3 and VNC server.  
# Lvious  
# Pull base image.  
FROM ubuntu:16.04  
RUN set -xe && echo '#!/bin/sh' > /usr/sbin/policy-rc.d && echo 'exit 101' >>
/usr/sbin/policy-rc.d && chmod +x /usr/sbin/policy-rc.d && dpkg-divert --local
\--rename --add /sbin/initctl && cp -a /usr/sbin/policy-rc.d /sbin/initctl &&
sed -i 's/^exit.*/exit 0/' /sbin/initctl && echo 'force-unsafe-io' >
/etc/dpkg/dpkg.cfg.d/docker-apt-speedup && echo 'DPkg::Post-Invoke { "rm -f
/var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb
/var/cache/apt/*.bin || true"; };' > /etc/apt/apt.conf.d/docker-clean && echo
'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb
/var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >>
/etc/apt/apt.conf.d/docker-clean && echo 'Dir::Cache::pkgcache "";
Dir::Cache::srcpkgcache "";' >> /etc/apt/apt.conf.d/docker-clean && echo
'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages && echo
'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' >
/etc/apt/apt.conf.d/docker-gzip-indexes  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN sed -i 's/^#\s*\\(deb.*universe\\)$/\1/g' /etc/apt/sources.list  
  
CMD ["/bin/bash"]  
  
# Setup enviroment variables  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV USER=root  
  
RUN apt-get update && apt-get install -y --no-install-recommends ubuntu-
desktop && apt-get install -y gnome-panel gnome-settings-daemon metacity
nautilus gnome-terminal && apt-get install -y tightvncserver && apt-get
install -y expect && mkdir /root/.vnc  
  
#Update the package manager and upgrade the system  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get update  
  
ADD https://raw.githubusercontent.com/Lvious/Dockerfile-Ubuntu-
Gnome/master/xstartup /root/.vnc/xstartup  
  
ADD https://raw.githubusercontent.com/Lvious/Dockerfile-Ubuntu-
Gnome/master/spawn-desktop.sh /usr/local/etc/spawn-desktop.sh  
  
ADD https://raw.githubusercontent.com/Lvious/Dockerfile-Ubuntu-
Gnome/master/start-vnc-expect-script.sh /usr/local/etc/start-vnc-expect-
script.sh  
  
RUN chmod 755 /root/.vnc/xstartup && chmod +x /usr/local/etc/start-vnc-expect-
script.sh && chmod +x /usr/local/etc/spawn-desktop.sh  
  
CMD bash -C '/usr/local/etc/spawn-desktop.sh';'bash'  
  
# Expose ports.  
EXPOSE 5901/tcp  


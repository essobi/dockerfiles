FROM fedora:26  
MAINTAINER Michael Batz <mail@michael-batz.de>  
  
# locale settings  
ARG build_locale=de_DE  
ARG build_timezone=Europe/Berlin  
  
# set locales  
ENV LANG ${build_locale}.utf8  
  
# setup  
RUN dnf -y group install xfce-desktop \  
&& dnf -y install \  
# locales  
glibc-locale-source langpacks-de.noarch langpacks-en.noarch \  
# x2go and required tools  
x2goserver.x86_64 x2goserver-xsession.x86_64 passwd \  
# tools for usage  
openssh-clients.x86_64 telnet.x86_64 \  
firefox.x86_64 chromium.x86_64 \  
# setup locales  
&& localedef -c -i ${build_locale} -f UTF-8 ${build_locale}.utf-8 \  
&& rm /etc/localtime \  
&& ln -s /usr/share/zoneinfo/${build_timezone} /etc/localtime \  
# generate host keys  
&& ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' \  
&& ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' \  
&& ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N '' \  
# create directory for dbus  
&& mkdir -p /run/dbus \  
# cleanup for a smaller image  
&& dnf -y clean all  
  
# copy start script  
COPY scripts/* /opt/container/  
  
# execute run.sh  
CMD ["/opt/container/run.sh"]  


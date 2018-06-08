FROM debian:testing-slim  
MAINTAINER marthym@github.com  
  
# Tweak APT  
RUN sed -i 's/http.debian.net/ftp.fr.debian.org/g' /etc/apt/sources.list && \  
echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
echo "APT::Install-Recommends \"0\";" >> /etc/apt/apt.conf.d/99_norecommends
&& \  
echo "APT::Install-Suggests \"0\";" >> /etc/apt/apt.conf.d/99_norecommends &&
\  
echo "deb http://ftp.debian.org/debian/ wheezy main contrib non-free" >>
/etc/apt/sources.list.d/wheezy.list && \  
echo "deb http://ftp.debian.org/debian/ jessie contrib non-free" >>
/etc/apt/sources.list.d/jessie-non-free.list  
  
RUN touch /etc/inittab  
  
# Update dependency  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt -y update && \  
apt -y install runit curl vim-tiny procps && \  
apt clean && \  
apt autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Remove installed runit services  
RUN rm -Rf /etc/sv/*  
  
CMD ["/usr/bin/runsvdir", "-P", "/etc/sv"]  


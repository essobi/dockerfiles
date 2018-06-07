FROM debian:jessie  
ENV DEBIAN_FRONTEND noninteractive  
  
# Download & install required applications: curl, sudo.  
RUN apt-get -qqy update  
RUN apt-get -qqy install wget python sudo  
  
# Create service account and set permissions.  
RUN useradd -d /dbox -c "Dropbox Daemon Account" -s /usr/sbin/nologin dropbox  
RUN mkdir -p /dbox/.dropbox /dbox/.dropbox-dist /dbox/Dropbox /dbox/base  
  
# Download & install current version of dropbox.  
RUN wget -nv -O /dbox/base/dropbox.tar.gz
"https://www.dropbox.com/download?plat=lnx.x86_64"  
RUN wget -nv -O /dbox/dropbox.py
"https://www.dropbox.com/download?dl=packages/dropbox.py"  
  
# Perform image clean up.  
RUN apt-get -qqy autoclean  
  
# Set permissions  
RUN chown -R dropbox /dbox  
  
# Install script for managing dropbox init.  
COPY run /dbox/  
COPY dropbox /usr/local/bin/  
RUN chmod +x /dbox/run /usr/local/bin/dropbox /dbox/dropbox.py  
  
VOLUME ["/dbox/.dropbox", "/dbox/.dropbox-dist", "/dbox/Dropbox"]  
  
# Dropbox Lan-sync  
EXPOSE 17500  
CMD ["/dbox/run"]  


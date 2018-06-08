FROM ubuntu:16.04  
MAINTAINER Sebastian Schneider <mail@sesc.eu>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen en_US en_US.UTF-8 && dpkg-reconfigure locales  
  
RUN apt-get update && apt-get install -y \  
sane \  
sane-utils \  
libsane-extras \  
libsane-hpaio \  
dbus \  
avahi-utils \  
supervisor \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN adduser saned scanner \  
&& adduser saned lp \  
&& chown saned:lp /etc/sane.d/saned.conf /etc/sane.d/dll.conf  
  
COPY configure.sh /configure.sh  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 6566 10000 10001  
# Make sure, that the device node e.g. /dev/usb/00x/ have group id 7 (lp) and
group read access.  
# Environment variable:  
# SANED_ACL - [required] IP ranges or hosts that are allowed access to the
daemon.  
# SANED_DEVICE - [required] The device as reported by 'scanimage -L' to use
for scanning via network.  
# SANED_DLL - [optional] Overwrite /etc/sane.d/dll.conf with these values for
faster response of saned.  
#  
# docker run --device /dev:/dev --privileged -e
SANED_ACL="192.168.0.0/24\n10.0.0.0/8" -e SANED_DEVICE="hpaio:xxx" -e
SANED_DLL="hp\hpaio" sesceu/saned  


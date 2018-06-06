FROM debian:testing  
  
MAINTAINER Ian Reinhart Geiser <geiseri@yahoo.com>  
  
EXPOSE 3389  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV container docker  
  
# setup debian  
RUN \  
apt-get -q update && \  
apt-get install -yq \  
locales xrdp x-window-system-core desktop-base sudo \  
xfonts-100dpi xfonts-100dpi-transcoded xfonts-75dpi xfonts-75dpi-transcoded
xfonts-base \  
openbox tint2 \  
cloud-init  
  
# cloud init  
ADD cloud-init/cloud.cfg /etc/cloud/cloud.cfg  
ADD cloud-init/user-data /var/lib/cloud/seed/nocloud/user-data  
ADD cloud-init/meta-data /var/lib/cloud/seed/nocloud/meta-data  
ADD cloud-init/first-run.sh /usr/bin/first-run.sh  
RUN chmod +x /usr/bin/first-run.sh  
  
# configure desktop  
ADD desktop/openbox.rc.xml /etc/xdg/openbox/rc.xml  
ADD desktop/tint2rc /etc/xdg/tint2/tint2rc  
ADD desktop/tint2.sh /etc/X11/Xsession.d/91-tint2  
RUN chmod +x /etc/X11/Xsession.d/91-tint2  
  
# clean up apt  
RUN apt-get -yqq clean && \  
apt-get autoremove -yqq --purge && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# configure systemd  
ADD systemd/systemd-tmpfiles-setup.service /etc/systemd/system/systemd-
tmpfiles-setup.service.d/ignoresysfs.conf  
ADD systemd/limits.conf /etc/security/limits.conf  
RUN \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ "$i" !=
"systemd-tmpfiles-setup.service" ] && rm -fv $i; done); \  
rm -fv /lib/systemd/system/multi-user.target.wants/*; \  
rm -fv /etc/systemd/system/*.wants/*; \  
rm -fv /lib/systemd/system/local-fs.target.wants/*; \  
rm -fv /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -fv /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -fv /lib/systemd/system/basic.target.wants/*; \  
systemctl enable cloud-init.service && \  
systemctl enable cloud-config.service && \  
systemctl enable cloud-final.service && \  
systemctl set-default multi-user.target && \  
useradd --system -U syslog  
  
CMD ["/lib/systemd/systemd"]  


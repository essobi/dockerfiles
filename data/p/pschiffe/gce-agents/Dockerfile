FROM centos:7  
MAINTAINER "Peter Schiffer" <pschiffe@redhat.com>  
  
ENV NAME=gce-agents VERSION=0 RELEASE=0 ARCH=x86_64  
LABEL name="$FGC/$NAME" \  
version="$VERSION" \  
release="$RELEASE.$DISTTAG" \  
architecture="$ARCH" \  
summary="Packages for Google Compute Engine Linux images." \  
maintainer="Peter Schiffer <pschiffe@redhat.com>"  
  
COPY google-cloud.repo /etc/yum.repos.d/google-cloud.repo  
  
RUN yum -y --setopt=tsflags=nodocs install \  
ethtool \  
iproute \  
openssh \  
selinux-policy-targeted \  
google-compute-engine \  
&& yum clean all  
  
STOPSIGNAL SIGRTMIN+3  
ENV container=docker  
  
COPY manifest.json tmpfiles.template service.template config.json.template
/exports/  
COPY dbus.service install.service /etc/systemd/system/  
COPY run-in-host.sh install.sh /usr/local/bin/  
COPY google-accounts-daemon-config.conf /etc/systemd/system/google-accounts-
daemon.service.d/config.conf  
  
RUN rm -f /etc/machine-id /etc/fstab /var/lib/rpm/__db.* \  
&& mkdir -p /var/lib/google /run/secrets \  
&& systemctl enable install.service  
  
CMD [ "/usr/sbin/init" ]  


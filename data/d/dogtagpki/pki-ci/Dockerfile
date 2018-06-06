FROM registry.fedoraproject.org/fedora:28  
LABEL \  
name="dogtagpki/pki-ci:f28_106_46" \  
maintainer="Dinesh Prasanth M K <dmoluguw@redhat.com>" \  
vendor="Dogtag PKI" \  
url="http://dogtagpki.org/"  
# PYTHONCOERCECLOCALE warning  
ENV LC_ALL=C.UTF-8  
# install base dependencies and DS  
RUN echo 'deltarpm = false' >> /etc/dnf/dnf.conf \  
&& dnf update -y dnf \  
&& dnf install -y dnf-plugins-core sudo wget make rpm-build 389-ds-base\  
&& dnf config-manager --set-enabled updates-testing \  
&& dnf install -y python-srpm-macros \  
&& dnf install -y @buildsys-build @development-tools \  
&& dnf clean all  
  
# update all packages  
RUN dnf copr -y enable @pki/10.6 \  
&& dnf -y update  
  
# To avoid RPM errors  
RUN ls /var/lib/rpm/ \  
&& mv /var/lib/rpm/__db* /tmp/  
# install PKI build dependencies  
RUN dnf builddep -y pki-core  
  
# build env  
ENV BUILDDIR="/tmp/workdir" \  
BUILDUSER="builduser" \  
BUILDUSER_UID=1000 \  
BUILDUSER_GID=1000  
VOLUME ["${BUILDDIR}"]  
EXPOSE 389 8080 8443  
# https://raw.githubusercontent.com/fedora-cloud/Fedora-
Dockerfiles/master/systemd/systemd/Dockerfile  
ENV container docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*; \  
rm -f /etc/systemd/system/*.wants/*; \  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*; \  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# Install FreeIPA-4.6  
RUN dnf config-manager --set-disabled updates-testing \  
&& dnf install -y freeipa-server freeipa-server-dns freeipa-server-trust-ad
python3-ipatests --best --allowerasing \  
&& dnf clean all \  
&& for i in /usr/lib/systemd/system/*-domainname.service; \  
do sed -i 's#^ExecStart=/#ExecStart=-/#' $i ; done  
  
# update everything and try to resolve conflicts  
RUN dnf update -y --best --allowerasing \  
&& dnf clean all  
  
VOLUME [ "/sys/fs/cgroup", "/tmp", "/run", "/freeipa" ]  
STOPSIGNAL SIGRTMIN+3  
ENTRYPOINT [ "/usr/sbin/init" ]  


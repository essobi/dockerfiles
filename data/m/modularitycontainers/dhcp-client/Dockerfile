# Container artifact for the DHCP client module  
# This should probably become something like...:  
# FROM registry.fedoraproject.org/module-baseruntime:26  
# ...and probably would only have the repo of the module and (as the case may  
# be) its dependencies enabled.  
FROM baseruntime/baseruntime:latest  
  
# Notes: Current base-runtime images will enable a package repo with all  
# packages from the currently latest compose of Fedora 26/Boltron. Buyer  
# beware.  
  
ENV NAME=dhcp-client \  
VERSION=1.0 \  
RELEASE=1 \  
ARCH=x86_64 \  
INTERFACES=""  
  
LABEL summary="Provides the ISC DHCP client daemon" \  
name="$FGC/$NAME" \  
version="$VERSION" \  
release="$RELEASE.$DISTTAG" \  
architecture="x86_64" \  
maintainer="Karsten Hopp <karsten@redhat.com>" \  
vendor="Fedora Project" \  
com.redhat.component="dhcp" \  
org.fedoraproject.component="dhcp" \  
authoritative-source-url="registry.fedoraproject.org" \  
usage="docker run --net=host --cap-add=net_admin modularitycontainers/dhcp-
client-container" \  
io.k8s.description="A container with the DHCP client" \  
io.k8s.display-name="DHCP client (dhclient)"  
ADD files/rundhcp.sh /usr/sbin/rundhcp.sh  
  
# initscripts: for /etc/sysconfig/network-scripts  
RUN INSTALL_PKGS="dhcp-client initscripts" && \  
microdnf -y install $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
microdnf -y clean all && \  
chmod 755 /usr/sbin/rundhcp.sh && \  
chown daemon.daemon /var/lib/dhclient  
  
COPY root/help.1 /  
  
USER 0  
  
CMD ["/usr/sbin/rundhcp.sh"]  


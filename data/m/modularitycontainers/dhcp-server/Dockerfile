FROM registry.fedoraproject.org/fedora:26  
# dhcp-server image  
LABEL MAINTAINER Dominika Hodovska, Red Hat <dhodovsk@redhat.com>  
  
ENV DHCP_VERSION=4.3.5 \  
NAME=dhcp-server \  
VERSION=0 \  
RELEASE=1 \  
ARCH=x86_64  
  
LABEL summary="DHCP (Dynamic Host Configuration Protocol) server container" \  
name="$FGC/$NAME" \  
version="$VERSION" \  
Release="$RELEASE.$DISTTAG" \  
architecture="$ARCH" \  
com.redhat.component=$NAME \  
usage="docker run --net=host -v /etc/dhcp/:/etc/dhcp -v
/var/lib/dhcpd:/var/lib/dhcpd --name dhcp f26/dhcp-server" \  
description="dhcp-server provides network configuration for dhcp-clients" \  
vendor="Fedora Project" \  
org.fedoraproject.component="dhcp-server" \  
authoritative-source-url="registry.fedoraproject.org" \  
io.k8s.description="dhcp-server provides network configuration for dhcp-
clients" \  
io.k8s.display-name="dhcp-server" \  
io.openshift.tags="dhcp"  
  
COPY help.1 /  
ADD repos/dhcp-server-module.repo /etc/yum.repos.d/  
ADD files/dhcpd.sh /dhcpd  
  
RUN dnf install -y dhcp-server && dnf clean all && \  
chmod 755 /dhcpd  
  
VOLUME ['/etc/dhcp', '/etc/dhcp'] ['/var/lib/dhcpd', '/var/lib/dhcpd']  
  
CMD ["/dhcpd", "-d", "--no-pid"]  


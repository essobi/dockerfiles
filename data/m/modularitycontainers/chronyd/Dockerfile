FROM registry.fedoraproject.org/f26-modular/boltron  
  
# This is a container for minimal chrony module - a Network Time Protocol
Server.  
#  
# Volumes:  
# * /etc/chrony.conf - default configuration file for chronyd  
# Exposed ports:  
# * 123 - Network Time Protocol (NTP) - used for time synchronization  
# Linux capabilities:  
# * SYS_TIME - Set system clock  
  
LABEL MAINTAINER Karsten Hopp, Red Hat <karsten@redhat.com>  
  
# Enviroment variables  
ENV NAME="chronyd" RELEASE=1 ARCH=x86_64 VERSION=0  
  
LABEL summary="A minimal chrony module" \  
name="$FGC/$NAME" \  
version="$VERSION" \  
release="$RELEASE.$DISTTAG" \  
architecture="$ARCH" \  
com.redhat.component="$NAME" \  
usage="docker run --cap-add SYS_TIME -d f26/chronyd" \  
description="A container with the chrony NTP time server" \  
io.k8s.description="A container with the chrony NTP time server" \  
io.k8s.display-name="NTP server (chrony)" \  
io.openshift.expose-services="123" \  
io.openshift.tags="ntp, chronyd, time"  
RUN dnf install -y --nodocs chrony && \  
dnf -y clean all  
  
# Specify it during `docker run` as parameter: "-p
<host_port>:<container_port>"  
EXPOSE 123  
  
# VOLUME instruction creates unnamed volume and mounts it to the provided
path,  
# you can override this behavior by mounting  
# a selected host directory into container: "-v
<host_directory>:<container_directory>"  
VOLUME /etc/chrony.conf:/etc/chrony.conf:ro  
  
# Specify username which will be used during running container  
USER 0  
  
# Command which will start service during command `docker run`  
CMD ["/usr/sbin/chronyd", "-d"]  


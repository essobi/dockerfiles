FROM debian:jessie  
  
MAINTAINER newtork / Alexander Dümont <alexander_duemont@web.de>  
  
  
##########################################  
# #  
# Docker Build #  
# #  
##########################################  
  
#  
# USAGE  
# -----  
# docker pull newtork/group-domain-stub  
#  
#  
  
  
##########################################  
# #  
# Build Settings / Environment #  
# #  
##########################################  
  
#### Port Usage for samba active directory  
#  
# Service Port Protocol  
# -------------------- -------- --------  
# DNS 53 tcp/udp  
# Kerberos 88 tcp/udp  
# End Point Mapper 135 tcp  
# NetBIOS Name Service 137 udp  
# NetBIOS Datagram 138 udp  
# NetBIOS Session 139 tcp  
# LDAP 389 tcp/udp  
# SMB over TCP 445 tcp  
# Kerberos kpasswd 464 tcp/udp  
# LDAPS 636 tcp  
# Dynamic RPC Ports 1024-5000 tcp  
# Global Cataloge 3268 tcp  
# Global Cataloge SSL 3269 tcp  
  
EXPOSE 53 88 135 137 138 139 389 445 464 636 1024-1152 3268 3269  
  
# upload a sample kerberos configuration  
COPY krb5.conf /etc/  
  
  
  
##########################################  
# #  
# BUILD #  
# #  
##########################################  
  
#  
# Build-Process:  
# --------------  
#  
# 1) Just download and install required packages.  
#  
#  
  
  
RUN echo "Updating repositories..." && \  
apt-get -qqy update && \  
echo "Downloading Dependencies..." && \  
echo "(This may take a minute or two.)" && \  
apt-get -qqy install attr libattr1 libattr1-dev samba winbind bind9
krb5-admin-server krb5-kdc smbclient > /dev/null 2>&1 && \  
echo "Download Complete."


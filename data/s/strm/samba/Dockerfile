FROM debian:9.2  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
samba samba-common smbclient smbc smbldap-tools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Volumes  
VOLUME /data  
  
# Expose the samba to the network  
EXPOSE 137/udp 138/udp 139 445  
COPY main.sh /  
  
ENTRYPOINT ["/main.sh"]  


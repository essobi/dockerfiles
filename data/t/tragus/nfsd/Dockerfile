FROM tragus/webmin  
  
# We build this off of the webmin image which will give us an easy way to  
# administer our NFS server.  
MAINTAINER James Johnson  
  
RUN apt-get update && \  
apt-get -y install nfs-kernel-server  
  
EXPOSE 80/tcp 111/udp 111/tcp 2049/tcp 2049/udp  
  
# Perform build-time configuration of the container  
ADD nfsd.configure /usr/local/bin/nfsd.configure  
RUN chmod +x /usr/local/bin/nfsd.configure && /usr/local/bin/nfsd.configure  
  
# Install any other scripts  
ADD nfsd.start /usr/local/lib/container-controller/start/  
ADD nfsd.stop /usr/local/lib/container-controller/stop/  
  
ENTRYPOINT ["/usr/local/bin/container-controller.start"]  


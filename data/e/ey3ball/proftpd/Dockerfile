FROM ubuntu:latest  
MAINTAINER florian@ey3ball.net  
  
RUN apt-get update && \  
apt-get install -y proftpd wget && \  
wget http://packages.openmediavault.org/public/pool/main/p/proftpd-mod-
vroot/proftpd-mod-vroot_0.9.3-1_amd64.deb && \  
dpkg --force-depends -i proftpd-mod-vroot_0.9.3-1_amd64.deb && \  
rm -f proftpd-mod-vroot_0.9.3-1_amd64.deb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i -e 's/# PassivePorts.*/PassivePorts 6000 6010/g'
/etc/proftpd/proftpd.conf  
  
CMD ["-n"]  
ENTRYPOINT ["proftpd"]  
EXPOSE 21 6000 6001 6002 6003 6004 6005 6006 6007 6008 6009 6010  


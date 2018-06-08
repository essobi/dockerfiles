FROM gentoo/stage3-amd64:latest  
  
LABEL Description="This image tests the Xtreemfs overlay" Vendor="Patrick
Hieber" Version="0.1"  
  
RUN emerge --sync && \  
emerge -n layman && \  
layman -f && \  
layman -a xtreemfs && \  
echo "source /var/lib/layman/make.conf" >> /etc/portage/make.conf && \  
echo "=net-fs/xtreemfs-1.5 ~amd64" >> /etc/portage/package.keywords/xtreemfs
&& \  
emerge --autounmask-write xtreemfs && \  
etc-update --automode -5 && \  
emerge -q xtreemfs  


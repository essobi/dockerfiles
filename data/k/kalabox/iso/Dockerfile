# Build a custom boot2docker image for kalabox2  
#  
# docker build -t kalabox/iso .  
# docker run --rm kalabox/iso > kalabox.iso  
#  
FROM boot2docker/boot2docker  
  
#  
# Set a backup dns server to handle all sorts of chaos  
# This will slow stuff down since it require the hostprovided dns  
# server timeout first. Ultimately its better for the user  
# to just restart their VM.  
#  
# @todo: Not sure how this impacts other things like local dns a la intranet  
# or VPN  
#  
# https://github.com/boot2docker/boot2docker/issues/776  
# https://github.com/docker/machine/issues/1857  
#  
RUN \  
echo "# Assign a backup dns server" >> $ROOTFS/opt/bootsync.sh && \  
echo "echo \"nameserver 8.8.8.8\" >> /etc/resolv.conf" >>
$ROOTFS/opt/bootsync.sh && \  
echo "echo \"nameserver 8.8.4.4\" >> /etc/resolv.conf" >>
$ROOTFS/opt/bootsync.sh && \  
echo "echo \"options timeout:1 attempts:1\" >> /etc/resolv.conf" >>
$ROOTFS/opt/bootsync.sh  
  
#  
# Need to manually add in support for vbox file share automounting on linux  
# until the following is merged  
#  
# https://github.com/boot2docker/boot2docker/pull/1086  
#  
RUN rm -f $ROOTFS/etc/rc.d/vbox  
ADD vbox $ROOTFS/etc/rc.d/vbox  
RUN chmod +x $ROOTFS/etc/rc.d/vbox  
  
# Make all the iso  
RUN /make_iso.sh  
  
CMD ["cat", "boot2docker.iso"]  


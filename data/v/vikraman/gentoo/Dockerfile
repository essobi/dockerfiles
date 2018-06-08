FROM scratch  
  
MAINTAINER Vikraman  
  
# The stage3 release version  
ENV RELEASE 20160317  
# Use busybox binary as tar  
ADD bb /tar  
  
# Download stage3 tarball  
ADD
http://ftp.ussg.iu.edu/linux/gentoo/releases/amd64/autobuilds/${RELEASE}/stage3-amd64-${RELEASE}.tar.bz2
/stage3.tar.bz2  
  
# Exclude file for tar  
ADD exclude /  
  
# Extract stage3 tarball  
RUN ["/tar", "xjpf", "stage3.tar.bz2", "-X", "exclude"]  
  
# Cleanup  
RUN rm -f tar exclude stage3.tar.bz2  
  
# Setup the rc_sys  
RUN sed -e 's/#rc_sys=""/rc_sys="lxc"/g' -i /etc/rc.conf  
  
# By default, UTC system  
RUN echo 'UTC' > /etc/timezone  
  
# Setup the portage directory and permissions  
RUN mkdir -p /usr/portage/{distfiles,metadata,packages}  
RUN chown -R portage:portage /usr/portage  
RUN echo "masters = gentoo" > /usr/portage/metadata/layout.conf  
  
# Sync portage  
RUN emerge-webrsync -q  
  
# Display some news items  
RUN eselect news read new  
  
# Finalization  
RUN env-update  
  
# The glorious shell  
CMD ["/bin/bash"]  


From gentoo/stage3-amd64  
MAINTAINER Necrose99  
ENV ARCH=arm64  
VOLUME /var/lib/layman:rw, /usr/portage:rw", /usr/portage/distfiles:rw,
/chroot/packages:rw, /:rw  
VOLUME /chroot:rw /var/lib/entropy/client/packages:rw
/chroot/var/lib/entropy/client/packages:rw  
## Fuck Layman with fire least for now... its a royal pain in the ass to build
in docker sometimes , this give repos faster.  
## although layman is preferable. however as stale as gentoo's arm64 stage3
image is eassier is better...  
VOLUME /etc/portage/repos.conf:rw /chroot/etc/portage/repos.conf:rw
/chroot/usr/overlays/:rw /var/lib/layman:rw /chroot//var/lib/layman:rw  
## let portage pull them down...  
ADD https://github.com/mickael-guene/umeq/releases/download/1.7.4/umeq-arm64 /  
## add binformat to host and to chroot area  
ADD https://raw.githubusercontent.com/necrose99/Docker-Gentoo-
ARM64/master/build/qemu-arm64.conf /etc/binfmt.d/qemu-arm64.conf  
ADD https://raw.githubusercontent.com/necrose99/Docker-Gentoo-
ARM64/master/build/qemu-arm64.conf /chroot/etc/binfmt.d/qemu-arm64.conf  
  
ADD https://raw.githubusercontent.com/mickael-guene/proot-static-build/master-
umeq/static/proot-x86_64 /proot  
ADD
http://distfiles.gentoo.org/experimental/arm64/stage3-arm64-20180305.tar.bz2
/chroot/  
ADD https://github.com/necrose99/Arm64-Linux-prep/blob/master/prep.zip
/chroot/  
ADD https://raw.githubusercontent.com/Sabayon/docker-builder-
amd64/master/script/depcheck /chroot/usr/local/bin/depcheck  
#Add portage -into chroot.  
RUN mkdir -p /chroot/usr/portage/distfiles /chroot/usr/portage/metadata
/chroot/usr/portage/packages  
  
# Set locales to en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
# Set environment variables.  
ENV HOME /root  
# fire up the chroot  
ENTRYPOINT ["./proot -R /chroot/ -q ./umeq-arm64 /chroot/bin/bash"]  
  
# Setup the rc_sys , alredy done in gentoo official image , clone into chroot.  
RUN cp /etc/rc.conf/ chroot/etc/rc.conf  
  


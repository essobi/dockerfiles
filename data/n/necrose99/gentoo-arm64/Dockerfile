FROM scratch  
MAINTAINER Necrose99  
ENV ARCH=arm64  
VOLUME /var/lib/layman:rw, /usr/portage:rw", /usr/portage/distfiles:rw,
/packages:rw, /:rw  
VOLUME /var/lib/entropy/client/packages:rw  
### Emuhosting Targets add busybox-x86_64 to run some setups with bash-amd64  
ADD https://busybox.net/downloads/binaries/1.26.2-defconfig-
multiarch/busybox-x86_64 /busybox/busybox-x86_64  
###  
## Add emulation tools.  
ADD https://github.com/multiarch/qemu-user-
static/releases/download/v2.9.1/qemu-aarch64-static.tar.gz /qemu-static-arm64  
ADD https://github.com/mickael-guene/umeq/releases/download/1.7.5/umeq-arm64 /  
ADD https://github.com/mickael-guene/proot-static-
build/raw/master/static/proot-x86_64 /  
ADD
http://distfiles.gentoo.org/experimental/arm64/stage3-arm64-arm64-20170223.tar.bz2
/  
# ADD http://distfiles.gentoo.org/releases/arm/autobuilds/current-
stage3-arm64/stage3-arm64-20161219.tar.bz2 /  
## curent stable..  
# ADD https://github.com/necrose99/Arm64-Linux-prep/blob/master/prep.zip /  
## add more tools before the pre-op Linux virtual OS crashes off and wont have
emulation.  
ADD https://raw.githubusercontent.com/necrose99/Docker-Gentoo-
ARM64/master/build/qemu-arm64.conf /etc/binfmt.d/qemu-arm64.conf  
ENTRYPOINT ["./qemu-static-arm64", "-execve", "-0", "bash", "/bin/bash"]  
#Add portage  
  
  
# RUN wget http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2 /  
  
#RUN mkdir -p /usr/portage/distfiles /usr/portage/metadata
/usr/portage/packages  
#RUN bunzip2 -c /portage-latest.tar.bz2 | tar -xf - -C /usr  
#RUN rm /portage-latest.tar.bz2  
  
# Set locales to en_US.UTF-8  
#ENV LC_ALL=en_US.UTF-8  
# Set environment variables.  
#ENV HOME /root  
# fire up the chroot  
  
  
#https://hub.docker.com/r/mickaelguene/arm64-debian/~/dockerfile/  
  
#RUN ["/usr/bin/umeq-arm64", "-execve", "-0", "bash", "/bin/bash"]  
#CMD ["/usr/bin/umeq-arm64", "-execve", "-0", "bash", "/bin/bash"]  
#ADD https://raw.githubusercontent.com/necrose99/Docker-Gentoo-
ARM64/master/build.sh /build.sh  
#RUN /build.sh  
#  
# ADD https://raw.githubusercontent.com/Sabayon/docker-builder-
amd64/master/script/depcheck /chroot/usr/local/bin/depcheck  


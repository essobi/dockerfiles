  
FROM library/ubuntu-debootstrap:14.04  
MAINTAINER Anton Kozlov <drakon.mega@gmail.com>  
  
# Container utils  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
sudo \  
iptables \  
openssh-server  
  
# embox deps  
## base embox deps  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
bzip2 \  
unzip \  
python \  
curl \  
make \  
patch  
  
## x86 toolchain and all qemu's  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
gcc-multilib \  
gdb \  
qemu-system  
  
## arm crosscompiler  
RUN apt-get -y --no-install-recommends install \  
software-properties-common  
RUN add-apt-repository ppa:team-gcc-arm-embedded/ppa  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
"gcc-arm-embedded=6-2017q2-*"  
RUN apt-get -y autoremove software-properties-common  
  
## other crosscompilers  
RUN for a in microblaze mips powerpc sparc; do \  
curl -L
"https://github.com/embox/crosstool/releases/download/2.28-6.3.0-7.12/$a-elf-
toolchain.tar.bz2" | \  
tar -jxC /opt; \  
done  
  
## x86/test/lang  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
ruby \  
bison  
  
## x86/test/packetdrill  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
flex  
  
## usermode86/debug  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
bc  
  
## x86/test/fs  
RUN for i in $(seq 0 9); do \  
mknod /dev/loop$i -m0660 b 7 $i; \  
done  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
autoconf \  
pkg-config \  
mtd-utils \  
ntfs-3g  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt /var/cache/apt  
  
COPY create_matching_user.sh /usr/local/sbin/  
COPY docker_start.sh /usr/local/sbin/  
  
COPY id_rsa.pub /home/user/.ssh/authorized_keys  
COPY user.bashrc /home/user/.bashrc  
COPY user.bash_profile /home/user/.bash_profile  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
EXPOSE 22  
VOLUME /embox  
CMD ["/usr/local/sbin/docker_start.sh"]  


#  
# Copyright (C) 2015 HWPORT.COM  
# All rights reserved.  
#  
# Maintainers  
# JaeHyuk Cho ( <mailto:minzkn@minzkn.com> )  
#  
FROM ubuntu:12.04  
MAINTAINER JaeHyuk Cho <minzkn@minzkn.com>  
  
LABEL description="HWPORT Sigmadesigns dev environment"  
LABEL name="hwport/sigmadesigns:smp86xx"  
LABEL url="http://www.minzkn.com/"  
LABEL vendor="HWPORT"  
LABEL version="1.0"  
  
ARG DEBIAN_FRONTEND=noninteractive  
ARG TERM=xterm  
  
# let Upstart know it's in a container  
ENV container docker  
  
# ----  
RUN apt-get autoclean -y; \  
apt-get clean; \  
apt-get autoremove -y; \  
rm -rf /var/lib/apt/lists/*; \  
sed -i -e "s/archive\\.ubuntu\\.com/kr\\.archive\\.ubuntu\\.com/g"
"/etc/apt/sources.list"; \  
apt-get update --list-cleanup; \  
apt-get install -y apt-utils debconf-utils  
  
# we're going to want this bad boy installed so we can connect :)  
RUN apt-get install -y ssh; \  
sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional
pam_loginuid.so/' /etc/pam.d/sshd; \  
cp -f /etc/ssh/sshd_config /etc/ssh/sshd_config.org; \  
sed -ri "s/^PermitRootLogin\s+.*/PermitRootLogin yes/" /etc/ssh/sshd_config; \  
sed -i -e "s/^Port\s22$/Port 22\nPort 2222/g" /etc/ssh/sshd_config; \  
echo "AllowTcpForwarding yes" >> /etc/ssh/sshd_config; \  
echo "GatewayPorts yes" >> /etc/ssh/sshd_config; \  
echo "ClientAliveInterval 60" >> /etc/ssh/sshd_config; \  
echo "ClientAliveCountMax 3" >> /etc/ssh/sshd_config  
EXPOSE 22 2222  
ADD init-fake.conf /etc/init/fake-container-events.conf  
  
# undo some leet hax of the base image  
RUN rm /usr/sbin/policy-rc.d; \  
rm /sbin/initctl; \  
dpkg-divert --rename --remove /sbin/initctl  
  
# generate a nice UTF-8 locale for our use  
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8  
  
# remove some pointless services  
RUN /usr/sbin/update-rc.d -f ondemand remove; \  
for f in \  
/etc/init/u*.conf \  
/etc/init/mounted-dev.conf \  
/etc/init/mounted-proc.conf \  
/etc/init/mounted-run.conf \  
/etc/init/mounted-tmp.conf \  
/etc/init/mounted-var.conf \  
/etc/init/hostname.conf \  
/etc/init/networking.conf \  
/etc/init/tty*.conf \  
/etc/init/plymouth*.conf \  
/etc/init/hwclock*.conf \  
/etc/init/module*.conf\  
; do \  
dpkg-divert --local \--rename --add "$f"; \  
done; \  
echo '# /lib/init/fstab: cleared out for bare-bones Docker' > /lib/init/fstab  
  
# set a cheap, simple password for great convenience  
RUN echo 'root:docker.io' | chpasswd  
RUN /usr/sbin/useradd \  
-c "Default dev account" \  
-d "/home/dev" \  
-g users \  
-G users,adm,sudo \  
-m \  
-s /bin/bash \  
dev  
RUN echo "dev:duftlagl" | chpasswd  
  
# installing essential  
# already installed ? bash coreutils diffutils findutils  
RUN apt-get install -y \  
dpkg-dev \  
sudo \  
build-essential \  
binutils \  
gcc \  
g++ \  
libc-dev \  
gdb \  
perl \  
make \  
m4 \  
autoconf \  
automake \  
libtool \  
cmake \  
scons \  
bison \  
gawk \  
gettext \  
grep \  
sed \  
patch \  
linux-headers-generic \  
net-tools \  
vim \  
ccache \  
subversion \  
git \  
wget \  
curl \  
genromfs \  
rsync \  
texinfo \  
libncurses5-dev \  
ncurses-term \  
openssl \  
tar \  
gzip \  
bzip2 \  
xz-utils \  
unzip \  
zlib1g-dev \  
lib32z1 \  
cscope \  
exuberant-ctags \  
ftp  
#RUN apt-get install -y xmlto  
#RUN apt-get install -y libboost-dev  
#RUN apt-get install -y python-dev  
#RUN apt-get install -y python-software-properties  
# installing ftp server  
RUN echo "proftpd-basic shared/proftpd/inetd_or_standalone select standalone"
| debconf-set-selections; \  
apt-get install -y \  
proftpd  
RUN cp -f /etc/proftpd/proftpd.conf /etc/proftpd/proftpd.conf.org  
COPY ./proftpd.conf /etc/proftpd/proftpd.conf  
#COPY ./xproftpd /etc/xinet.d/xproftpd  
EXPOSE 21 65000 65001 65002 65003 65004 65005 65006 65007 65008 65009  
# installing xinetd service (with tftpd)  
#RUN apt-get install -y --no-install-recommends xinetd  
#RUN apt-get install tftpd  
#COPY ./tftp /etc/xinet.d/tftp  
#EXPOSE 69  
# install misc (optional)  
#RUN apt-get install -y libjpeg-dev  
#RUN apt-get install -y libpng-dev  
#RUN apt-get install -y libgif-dev  
#RUN apt-get install -y libssl-dev libcurl4-openssl-dev  
#RUN apt-get install -y libssh2-1-dev  
#RUN apt-get install -y libsqlite3-dev  
#RUN apt-get install -y freetds-dev  
#RUN apt-get install -y libpq-dev  
#RUN apt-get install -y libmysqlclient-dev  
#RUN apt-get install -y openjdk-7-jdk  
# install mips toolchain  
ADD https://sourcery.mentor.com/public/gnu_toolchain/mips-linux-
gnu/mips-4.3-51-mips-linux-gnu-i686-pc-linux-gnu.tar.bz2
/tmp/mips-4.3-51-mips-linux-gnu-i686-pc-linux-gnu.tar.bz2  
#COPY ./mips-4.3-51-mips-linux-gnu-i686-pc-linux-gnu.tar.bz2
/tmp/mips-4.3-51-mips-linux-gnu-i686-pc-linux-gnu.tar.bz2  
RUN tar -xjf /tmp/mips-4.3-51-mips-linux-gnu-i686-pc-linux-gnu.tar.bz2 -C
/opt; \  
rm -f /tmp/mips-4.3-51-mips-linux-gnu-i686-pc-linux-gnu.tar.bz2  
  
# clean meta  
RUN apt-get autoclean -y  
RUN apt-get clean  
RUN apt-get autoremove -y  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ----  
#VOLUME ["/test-share1", "/test-share2", "/test-share3"]  
# ----  
WORKDIR /  
CMD ["/sbin/init"]  
  
# ----  
# End of Dockerfile  


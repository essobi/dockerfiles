FROM debian:jessie  
ENV HOSTNAME osc  
RUN echo "HOSTNAME=${HOSTNAME}" > /etc/profile \  
&& SOURCES_LIST=/etc/apt/sources.list \  
&& echo "deb http://ftp.cn.debian.org/debian/ jessie main non-free contrib" >
${SOURCES_LIST} \  
&& echo "deb http://ftp.cn.debian.org/debian/ jessie-updates main non-free
contrib" >> ${SOURCES_LIST} \  
&& echo "deb-src http://ftp.cn.debian.org/debian/ jessie main non-free
contrib" >> ${SOURCES_LIST} \  
&& echo "deb-src http://ftp.cn.debian.org/debian/ jessie-updates main non-free
contrib" >> ${SOURCES_LIST} \  
&& echo "deb http://ftp.cn.debian.org/debian-security/ jessie/updates main
non-free contrib" >> ${SOURCES_LIST} \  
&& echo "deb-src http://ftp.cn.debian.org/debian-security/ jessie/updates main
non-free contrib" >> ${SOURCES_LIST} \  
&& echo 'osc' > /etc/hostname \  
&& echo '127.0.0.1 localhost' > /etc/hosts \  
&& echo '127.0.1.1 osc' >> /etc/hosts \  
&& echo '# The following lines are desirable for IPv6 capable hosts' >>
/etc/hosts \  
&& echo '::1 localhost ip6-localhost ip6-loopback' >> /etc/hosts \  
&& echo 'ff02::1 ip6-allnodes' >> /etc/hosts \  
&& echo 'ff02::2 ip6-allrouters' >> /etc/hosts \  
&& apt-get update \  
&& apt-get install -y \--force-yes --no-install-recommends \  
manpages manpages-dev bash-completion apt-utils \  
perl perl-modules \  
libtimedate-perl libdpkg-perl \  
gcc g++ \  
vim patch diffstat gawk subversion git-core colordiff file tree ctags global
bc chrpath openssh-client \  
python curl wget \  
lzma bzip2 xz-utils cpio ucf \  
dos2unix docbook-xsl xsltproc \  
dh-make debhelper pbuilder quilt debootstrap sbuild devscripts \  
gfortran gnupg gperf lintian \  
dpkg-sig u-boot-tools \  
libncurses5 libncurses5-dev ncurses-dev libssl-dev libc6 libc6-dev \  
libcap-dev libmount-dev libdbus-1-dev xutils-dev libgcc-4.9-dev \  
libgcrypt11* binutils-multiarch libfile-homedir-perl libconfig-auto-perl \  
dput emdebian-archive-keyring fakeroot build-essential \  
qemu qemu-user-static kmod kernel-package \  
bridge-utils net-tools uml-utilities openssh-server libc-dev linux-libc-dev \  
rpm pkg-config make autoconf automake pkgconf libtool \  
intltool autotools-dev dpkg-dev patchutils alien bison flex libbison-dev \  
libfl-dev libintl-perl libtext-unidecode-perl texinfo zip unzip \  
&& apt-get -y \--force-yes --no-install-recommends autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
RUN apt-get update \  
&& echo '#!/bin/bash' > /tmp/install_sudo.sh \  
&& echo 'apt-get install -y --no-install-recommends sudo <<EOF' >>
/tmp/install_sudo.sh \  
&& echo 'Y' >> /tmp/install_sudo.sh \  
&& echo 'EOF' >> /tmp/install_sudo.sh \  
&& chmod 777 /tmp/install_sudo.sh \  
&& /bin/bash /tmp/install_sudo.sh \  
&& rm /tmp/install_sudo.sh \  
&& apt-get -y \--force-yes --no-install-recommends autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
RUN echo '#!/bin/sh' > /tmp/adduser_osc-builder.sh \  
&& echo "echo 'osc ALL=(ALL:ALL) ALL' >> /etc/sudoers" >> /tmp/adduser_osc-
builder.sh \  
&& echo 'groupadd -g $1 osc' >> /tmp/adduser_osc-builder.sh \  
&& echo 'useradd -u $1 -g $2 -m -s /bin/bash osc' >> /tmp/adduser_osc-
builder.sh \  
&& echo 'passwd osc <<EOF' >> /tmp/adduser_osc-builder.sh \  
&& echo 'osc' >> /tmp/adduser_osc-builder.sh \  
&& echo 'osc' >> /tmp/adduser_osc-builder.sh \  
&& echo 'EOF' >> /tmp/adduser_osc-builder.sh \  
&& echo 'passwd root <<EOF2' >> /tmp/adduser_osc-builder.sh \  
&& echo 'root' >> /tmp/adduser_osc-builder.sh \  
&& echo 'root' >> /tmp/adduser_osc-builder.sh \  
&& echo 'EOF2' >> /tmp/adduser_osc-builder.sh \  
&& chmod 777 /tmp/adduser_osc-builder.sh  
  
RUN rm /bin/sh \  
&& ln -s /bin/bash /bin/sh \  
&& sh -c 'sed -ie "s/^UsePAM yes/UsePAM no/" /etc/ssh/sshd_config'  
MAINTAINER ZhuJiafa, zjfscu@gmail.com  


# x) - docker build -t ileonardo/base-ubuntu .  
# y) - Às Instruções fica nas Dependências e no final do arquivo: [REGRA] # z)  
### Base da Imagem  
FROM scratch  
  
### Autor  
MAINTAINER iLeonardo Carvalho <i.leonardo.c.c@outlook.com>  
  
ENV SET_LANG="en_US" \  
GEO="America" \  
REGIAO="Sao_Paulo" \  
\  
DEBIAN_FRONTEND="noninteractive" \  
INITRD="No" \  
FAKE_CHROOT="1"  
### Start  
# Adicionando a Imagem Oficial sem modificações  
# 2017-07-08 03:47 (44M)  
# http://cdimage.ubuntu.com/ubuntu-base/xenial/daily/current/xenial-base-
amd64.tar.gz  
# http://cdimage.ubuntu.com/ubuntu-base/xenial/daily/20170708/xenial-base-
amd64.tar.gz  
# Docker suporte em extrair tar.gz remoto (SOMENTE Local)  
ADD ["./xenial-base-amd64.tar.gz", "/"]  
ADD ["./root", "/root/"]  
ADD ["./skel", "/etc/skel/"]  
ADD ["./bash.bashrc", "/etc/"]  
  
# Arquivo inicial da execução do Docker  
CMD ["/bin/bash"]  
SHELL ["/bin/bash", "-c"]  
  
### Configurando a Imagem  
# Configure no init scripts to run on package updates  
RUN { \  
echo '#!/bin/sh'; \  
echo 'exit 101'; \  
} > /usr/sbin/policy-rc.d; \  
chmod +x /usr/sbin/policy-rc.d; \  
# a few minor docker-specific tweaks  
# see https://github.com/docker/docker/blob/master/contrib/mkimage/debootstrap  
dpkg-divert --local --rename --add /sbin/initctl; \  
  
cp -a /usr/sbin/policy-rc.d /sbin/initctl; \  
  
sed -i 's/^exit.*/exit 0/' /sbin/initctl; \  
  
  
echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup; \  
  
{ \  
echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb
/var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };'; \  
echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb
/var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };'; \  
echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";'; \  
} > /etc/apt/apt.conf.d/docker-clean; \  
  
  
echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages; \  
  
  
echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' >
/etc/apt/apt.conf.d/docker-gzip-indexes; \  
### Preparando  
# Work around initramfs-tools running on kernel 'upgrade':
<http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>  
mkdir -p /etc/container_environment; \  
echo -n "no" > /etc/container_environment/INITRD; \  
# Fix some issues with APT packages.  
# See https://github.com/dotcloud/docker/issues/1024  
dpkg-divert --local --rename --add /sbin/initctl; \  
ln -sf /bin/true /sbin/initctl; \  
# Replace the 'ischroot' tool to make it always return true.  
# Prevent initscripts updates from breaking /dev/shm.  
# https://journal.paul.querna.org/articles/2013/10/15/docker-ubuntu-on-
rackspace/  
# https://bugs.launchpad.net/launchpad/+bug/974584  
dpkg-divert --local --rename --add /usr/bin/ischroot; \  
ln -sf /bin/true /usr/bin/ischroot; \  
# UTF8  
locale-gen ${SET_LANG} ${SET_LANG}.UTF-8; \  
update-locale LANG=${SET_LANG}.UTF-8 LC_CTYPE=${SET_LANG}.UTF-8; \  
  
echo -n ${SET_LANG}.UTF-8 > /etc/container_environment/LANG; \  
echo -n ${SET_LANG}.UTF-8 > /etc/container_environment/LC_CTYPE; \  
# TimeZone  
ln -sf /usr/share/zoneinfo/${GEO}/${REGIAO} /etc/localtime; \  
echo "${GEO}/${REGIAO}" > /etc/timezone; \  
### Limpando os Pacotes desnecessários  
apt remove -qqy --allow-remove-essential \  
util-linux \  
ncurses-bin \  
initscripts \  
bsdutils \  
sysvinit-utils \  
ncurses-base \  
mount \  
makedev \  
login \  
libcryptsetup4 \  
libuuid1 \  
libudev1 \  
libss2 \  
libsmartcols1 \  
libseccomp2 \  
libncursesw5 \  
libncurses5 \  
libkmod2 \  
libgpg-error0 \  
libgcrypt20 \  
libdebconfclient0 \  
libcomerr2 \  
libcap2-bin \  
libapparmor1 \  
insserv \  
e2fslibs \  
diffutils; \  
### Configurações Essenciais  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list; \  
sed -i 's/# \\(.*universe$\\)/\1/g' /etc/apt/sources.list; \  
apt-get update; apt-get --no-install-recommends -qqy install \  
net-tools \  
iputils-ping \  
procps \  
vim-tiny; \  
  
ln -s /usr/bin/vim.tiny /usr/bin/vim; \  
### Limpando o cache  
apt-get -qqy autoremove; \  
apt-get autoclean; \  
apt-get clean; \  
rm -rf \  
/var/lib/apt/lists/* \  
/var/cache/apt/archives/* \  
/usr/share/doc/* \  
/usr/share/man/* \  
/tmp/* \  
/var/tmp/*;


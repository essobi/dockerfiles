FROM fedora:27  
  
ENV USER aallrd  
ENV GROUP aallrd  
ENV HOME /home/aallrd  
ENV HOSTNAME fooswan  
ENV TERM screen-256color  
ENV LANG=en_US.utf8  
  
# avoiding dnf proxy issues  
RUN echo "fastestmirror=true" >> /etc/dnf/dnf.conf \  
&& echo "timeout=500" >> /etc/yum.conf \  
&& echo "minrate=1" >> /etc/yum.conf  
  
# installing basic requirements for this dockerfile  
RUN dnf -y update \  
&& dnf -y upgrade \  
&& dnf -y install \  
basesystem \  
bash \  
coreutils \  
sed \  
gawk \  
grep \  
gzip \  
tar \  
unzip \  
curl \  
wget \  
less \  
sudo \  
hostname \  
which \  
xz \  
gettext \  
git \  
ctags \  
elfutils \  
indent \  
bzip2 \  
cpio \  
findutils \  
info \  
make \  
cmake \  
autoconf \  
automake \  
binutils \  
bison \  
flex \  
gcc \  
gcc-c++ \  
gdb \  
glibc \  
glibc-devel \  
libtool \  
pkgconf \  
patch \  
diffutils \  
ncurses \  
util-linux \  
vim-minimal \  
audit \  
filesystem \  
rootfiles \  
initscripts \  
fedora-release \  
dhcp-client \  
dnf \  
dnf-yum \  
iproute \  
iputils \  
kbd \  
man-db \  
openssh-clients \  
openssh-server \  
passwd \  
procps-ng \  
selinux-policy-targeted \  
setup \  
sssd-common \  
sssd-kcm \  
systemd \  
rpm \  
shadow-utils \  
policycoreutils \  
util-linux-user \  
&& dnf clean all  
  
# configuring hostname and user  
RUN echo ${HOSTNAME} > /etc/hostname \  
&& groupadd -g 1000 ${GROUP} \  
&& useradd -u 1000 -r --gid 1000 -G wheel -m -d ${HOME} -s /bin/bash -c
"System User" ${USER} \  
&& echo ${USER}:${USER} | chpasswd \  
&& sed -i 's/^#\s*\\(%wheel\s\\+ALL=(ALL)\s\\+NOPASSWD:\s\\+ALL\\)/\1/'
/etc/sudoers \  
&& chmod -R 755 ${HOME} \  
&& chsh --shell /bin/bash ${USER}  
  
# installing ssh  
ENV NOTVISIBLE "in users profile"  
RUN mkdir -p /var/run/sshd \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& echo "export VISIBLE=now" >> /etc/profile \  
&& ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa \  
&& ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa  
  
ARG CACHEBUST=1  
RUN su - ${USER} -c "$(curl -fsSL
https://raw.githubusercontent.com/aallrd/dotfiles/master/bootstrap) && cd
~/dotfiles && make"  
  
ADD start_sshd.sh /root/start_sshd.sh  
CMD ["/root/start_sshd.sh"]


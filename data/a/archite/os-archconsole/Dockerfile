FROM base/archlinux  
ARG COUNTRY=US  
ARG LOCALE=en_US.UTF-8  
ARG TZ=US/Pacific  
RUN pacman -Syu --noconfirm bash bash-completion ca-certificates curl htop
iproute2 iptables kmod less openssh psmisc rsync sudo util-linux vim  
RUN rm -rf /etc/ssh/*key*  
RUN groupadd -g 1100 rancher && \  
groupadd -g 1101 docker && \  
groupadd -r sudo && \  
useradd -u 1100 -g rancher -G sudo -s /bin/bash rancher && \  
usermod -aG docker rancher && \  
useradd -u 1101 -g docker -G sudo -s /bin/bash docker && \  
usermod -aG docker docker && \  
sed -i 's/rancher:!/rancher:*/g' /etc/shadow && \  
sed -i 's/docker:!/docker:*/g' /etc/shadow && \  
echo ClientAliveInterval 180 >> /etc/ssh/sshd_config && \  
echo '## allow password less for rancher user' >> /etc/sudoers && \  
echo 'rancher ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \  
echo '## allow password less for docker user' >> /etc/sudoers && \  
echo 'docker ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \  
echo 'ssh-keygen -A' >> /usr/sbin/update-ssh-keys && \  
ln -sfr /usr/bin/vim /usr/bin/vi && \  
curl -s
"https://www.archlinux.org/mirrorlist/?country=${COUNTRY}&protocol=http&protocol=https&ip_version=4"
| sed 's/^#Server/Server/g' | \  
rankmirrors -n 5 - | tee /etc/pacman.d/mirrorlist && \  
echo "LANG=${LOCALE}" > /etc/locale.conf && \  
sed -i "s/^#${LOCALE}/${LOCALE}/" /etc/locale.gen && \  
locale-gen && \  
ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime  
ENTRYPOINT ["/usr/bin/ros", "entrypoint"]  


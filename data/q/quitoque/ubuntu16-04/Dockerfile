FROM ubuntu:16.04  
  
MAINTAINER Rémi Chomat <remi@quitoque.fr>  
  
ENV HOME /root  
  
RUN apt-get update && \  
apt-get install -qq -y --no-install-recommends \  
acl vim emacs-nox wget curl less git \  
htop zip cron screen tree nano iotop \  
bash-completion jpegoptim optipng \  
openssh-server locales tzdata && \  
apt-get -qq -y autoremove && apt-get -qq -y autoclean && \  
apt-get -qq -y clean && rm -rf /var/lib/apt/lists/* && \  
sed -i 's/^PermitRootLogin/# PermitRootlogin/' /etc/ssh/sshd_config && \  
sed -Ei 's/^#?PasswordAuthentication.*$/PasswordAuthentication no/'
/etc/ssh/sshd_config && \  
echo 'root:root' | chpasswd && \  
mkdir -p /root/.ssh /var/run/sshd && \  
locale-gen fr_FR.UTF-8 && \  
useradd --system --uid=1000 -s /bin/bash -m -d /home/quitoque quitoque && \  
usermod -a -G root quitoque && usermod -a -G adm quitoque && \  
echo 'quitoque:quitoque' | chpasswd && \  
mkdir -p /home/quitoque/.ssh && \  
chown -R quitoque:quitoque /home/quitoque/.ssh && \  
echo "Europe/Paris" > /etc/timezone && \  
cp /usr/share/zoneinfo/Europe/Paris /etc/localtime  
  
# Set locales  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR:fr  
ENV LC_ALL fr_FR.UTF-8  
# Copy files as gitconfig, emacs.conf, vimrc, ...  
COPY ./files/emacs.conf /home/quitoque/.emacs  
COPY ./files/vimrc.conf /etc/vim/vimrc  
COPY ./files/gitconfig /home/quitoque/.gitconfig  
  
# Active the port 22 for the SSH  
EXPOSE 22  


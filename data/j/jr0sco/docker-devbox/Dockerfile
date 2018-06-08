FROM debian:stable  
MAINTAINER joel.cumberland <mr.jrosco@gmail.com>  
  
# Distro  
#ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
  
# Common packages  
RUN apt-get install -q -y \  
sudo \  
wget \  
vim \  
python \  
python-dev \  
python-pip \  
python3-pip \  
python-virtualenv \  
openssh-server\  
git-core \  
zsh \  
tmux \  
htop \  
pep8 \  
golang \  
python-sphinx \  
aptitude \  
locales \  
rubygems \  
ruby-dev \  
linkchecker \  
links \  
unzip \  
curl \  
yaml-mode \  
netcat \  
s3cmd \  
bc \  
u-boot-tools \  
libncurses-dev \  
w3m \  
&& apt-get clean -q -y  
  
# Locales  
RUN sed -i 's/# \\(en_US.UTF-8.*\\)/\1/' /etc/locale.gen \  
&& locale-gen en_US en_US.UTF-8  
# Setup user joelc  
RUN yes | adduser --disabled-password joelc --shell /bin/zsh \  
&& mkdir -p /home/joelc/.ssh/ \  
&& mkdir -p /home/joelc/.config/htop \  
&& wget https://github.com/jrosco.keys -O /home/joelc/.ssh/authorized_keys \  
&& chown -R joelc:joelc /home/joelc \  
&& chmod 700 /home/joelc/.ssh \  
&& chmod 600 /home/joelc/.ssh/authorized_keys \  
&& echo '%joelc ALL= NOPASSWD: ALL' >> /etc/sudoers \  
&& sudo -u joelc sh -c 'cd /home/joelc ; wget http://install.ohmyz.sh -O - |
sh || true'  
  
# Confs and files  
ADD confs/motd /etc/motd  
ADD confs/gitconfig /home/joelc/.gitconfig  
ADD confs/zsh /home/joelc/.zshrc  
ADD confs/htoprc /home/joelc/.config/htop/htoprc  
RUN chown joelc:joelc /home/joelc/.gitconfig /home/joelc/.zshrc  
  
ADD bin/init /init-container  
  
EXPOSE 22 2000  
  
ENTRYPOINT ["/init-container"]  


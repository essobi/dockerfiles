FROM phusion/baseimage:0.9.22  
MAINTAINER Sergi Blanco-Cuaresma <marblestation@users.noreply.github.com>  
USER root  
  
### SYSTEM / NETWORK / DEV TOOLS
################################################  
##-------------------------------------------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -o Dpkg::Options::="--force-
confold" && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
sudo \  
wget \  
ca-certificates \  
apt-transport-https \  
git \  
x11-apps && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
build-essential \  
gfortran \  
libncurses5-dev \  
libblas-dev \  
liblapack-dev \  
libatlas-base-dev \  
libfreetype6-dev \  
#tk-dev \  
libpng-dev \  
libhdf5-dev \  
#  
htop \  
locales \  
libssl-dev \  
curl \  
bash-completion \  
file \  
git-gui \  
tig \  
#vim \  
exuberant-ctags \  
tmux \  
less \  
rsync \  
sqlite3 \  
openssh-client \  
sshfs \  
net-tools \  
iputils-ping \  
psmisc && \  
#  
sed -i -e "s/#user_allow_other/user_allow_other/g" /etc/fuse.conf && \  
#  
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
&& \  
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
#-------------------------------------------------------------------------------  
################################################################################  
  
  
  
## VIM 8.0
#####################################################################  
#-------------------------------------------------------------------------------  
RUN add-apt-repository -y ppa:jonathonf/vim && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
vim  
#-------------------------------------------------------------------------------  
################################################################################  
  
  
  
## PYTHON
######################################################################  
#-------------------------------------------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
python \  
python-dev \  
python-virtualenv \  
python-tk \  
#python-qt4 \  
python-pip \  
python-numpy \  
python-scipy \  
python-matplotlib \  
python-pandas \  
python-setuptools && \  
pip install --upgrade pip && \  
pip install --upgrade numpy && \  
pip install --upgrade scipy && \  
pip install --upgrade matplotlib && \  
pip install --upgrade pandas && \  
pip install tables && \  
pip install wheel && \  
pip install jupyter && \  
pip install astropy && \  
pip install pudb && \  
pip install cython && \  
pip install pyflakes && \  
pip install scikit-learn && \  
pip install lockfile && \  
pip install patsy && \  
pip install statsmodels  
#-------------------------------------------------------------------------------  
################################################################################  
  
## Latex
#######################################################################  
#-------------------------------------------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
texlive texlive-bibtex-extra texlive-fonts-extra texlive-latex-extra texlive-
publishers \  
texlive-generic-recommended tex-gyre \  
latexmk \  
texlive texlive-lang-french texlive-lang-spanish  
#-------------------------------------------------------------------------------  
################################################################################  
  
  
  
## GOLANG
######################################################################  
#-------------------------------------------------------------------------------  
ENV GOLANG_VERSION 1.9  
RUN curl -sLO https://golang.org/dl/go${GOLANG_VERSION}.linux-amd64.tar.gz &&
\  
tar -C /usr/local -xzf go${GOLANG_VERSION}.linux-amd64.tar.gz && \  
rm -f go${GOLANG_VERSION}.linux-amd64.tar.gz  
#-------------------------------------------------------------------------------  
################################################################################  
  
  
  
## WEB DEVELOPMENT
#############################################################  
#-------------------------------------------------------------------------------  
# NodeJS  
RUN apt-get install -y --no-install-recommends nodejs nodejs-legacy npm  
#-------------------------------------------------------------------------------  
################################################################################  
  
  
  
## FINAL SETUP
#################################################################  
#-------------------------------------------------------------------------------  
# Cleaning  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean && \  
DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \  
rm -rf \  
/root/.cache/* \  
/tmp/* \  
/var/tmp/*  
#/var/lib/apt/lists/*  
#-------------------------------------------------------------------------------  
# Script to setup git  
COPY scripts/010_git_setup.sh /etc/my_init.d/010_git_setup.sh  
#-------------------------------------------------------------------------------  
# Create a docker user to run things as  
  
RUN useradd -m -s /bin/bash -U -G users ubuntu && echo "ubuntu ALL=(ALL)
NOPASSWD:ALL" > /etc/sudoers.d/users  
  
ENV LANG en_US.utf8  
USER ubuntu  
  
### RUST
########################################################################  
##-------------------------------------------------------------------------------  
#RUN curl https://sh.rustup.rs -sSf | sh -s -- -y  
##-------------------------------------------------------------------------------  
#################################################################################  
  
# Vim setup for the user  
RUN cd /home/ubuntu/ && \  
mkdir -p .ssh/ && \  
mkdir -p .vim/undodir/ && \  
mkdir -p .vim/spell/ && \  
mkdir -p .vim/autoload/ && \  
cd /home/ubuntu/.vim/autoload && \  
wget --quiet https://raw.githubusercontent.com/junegunn/vim-
plug/master/plug.vim && \  
cd /home/ubuntu/ && \  
wget --quiet https://raw.githubusercontent.com/marblestation/vim-complex-
sensible/master/vimrc -O .vim/vimrc && \  
ln -s .vim/vimrc .vimrc && \  
cd /home/ubuntu/.vim/spell/ && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/en.utf-8.spl && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/en.utf-8.sug && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/es.utf-8.spl && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/es.utf-8.sug && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/fr.utf-8.spl && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/fr.utf-8.sug && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/ca.utf-8.spl && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/ca.utf-8.sug && \  
cd /home/ubuntu/ && \  
vim +PlugInstall +qall  
  
COPY configurations/tmux.conf /home/ubuntu/.tmux.conf  
COPY configurations/bash_profile /home/ubuntu/.bash_profile  
RUN cd /home/ubuntu/ && \  
echo "source \$HOME/.bash_profile" >> /home/ubuntu/.bashrc && \  
git clone https://github.com/magicmonty/bash-git-prompt.git
/home/ubuntu/.bash-git-prompt --depth=1  
  
USER root  
RUN chown -R ubuntu:ubuntu /home/ubuntu/  
  
WORKDIR /home/ubuntu/  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
################################################################################  


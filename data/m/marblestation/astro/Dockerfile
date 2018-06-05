FROM ubuntu:16.04  
MAINTAINER Sergi Blanco-Cuaresma <marblestation@users.noreply.github.com>  
USER root  
  
## SYSTEM / NETWORK / DEV TOOLS
################################################  
#-------------------------------------------------------------------------------  
RUN apt-get update && \  
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
sudo \  
htop \  
locales \  
ca-certificates \  
apt-transport-https \  
libssl-dev \  
wget \  
curl \  
bash-completion \  
file \  
git \  
git-gui \  
#vim \  
# required to add a ppa:  
software-properties-common \  
exuberant-ctags \  
tmux \  
less \  
rsync \  
sqlite3 \  
openssh-client \  
sshfs \  
net-tools \  
iputils-ping \  
psmisc \  
x11-apps && \  
# Install Tini which will be PID 0 (in charge of killing zombie processes and
sending signals from outside the container)  
wget --quiet https://github.com/krallin/tini/releases/download/v0.10.0/tini &&
\  
echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini && \  
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
pip install pudb  
#-------------------------------------------------------------------------------  
################################################################################  
  
  
  
## ASTRONOMY
###################################################################  
#-------------------------------------------------------------------------------  
# Latex  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
texlive texlive-bibtex-extra texlive-fonts-extra texlive-latex-extra texlive-
publishers \  
latexmk \  
texlive texlive-lang-french texlive-lang-spanish  
#-------------------------------------------------------------------------------  
# Astrometry.net requires python with astro requirements  
COPY requirements_astro.txt requirements_astro.txt  
RUN pip install -r requirements_astro.txt  
#...............................................................................  
COPY scripts/install_astrometry.sh install_astrometry.sh  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
libbz2-dev \  
libcfitsio3-dev \  
libcairo2-dev \  
netpbm && \  
bash install_astrometry.sh  
#-------------------------------------------------------------------------------  
COPY scripts/install_astrotools.sh install_astrotools.sh  
RUN bash install_astrotools.sh  
#-------------------------------------------------------------------------------  
COPY scripts/install_sextractor.sh install_sextractor.sh  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
libfftw3-dev \  
liblapacke-dev && \  
bash install_sextractor.sh  
#-------------------------------------------------------------------------------  
COPY scripts/iraf /usr/local/bin/iraf  
COPY scripts/install_iraf.sh install_iraf.sh  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
tcsh \  
libxss1 && \  
bash install_iraf.sh && \  
chmod 755 /usr/local/bin/iraf  
#-------------------------------------------------------------------------------  
#COPY astrometry_index_4200 /opt/astrometry_catalogue/  
################################################################################  
  
  
  
## RUST
########################################################################  
#-------------------------------------------------------------------------------  
ENV RUST_VERSION 1.12.0  
RUN curl -sO https://static.rust-
lang.org/dist/rust-${RUST_VERSION}-x86_64-unknown-linux-gnu.tar.gz && \  
tar -xzf rust-${RUST_VERSION}-x86_64-unknown-linux-gnu.tar.gz && \  
./rust-${RUST_VERSION}-x86_64-unknown-linux-gnu/install.sh --without=rust-docs
&& \  
rm -rf \  
rust-${RUST_VERSION}-x86_64-unknown-linux-gnu \  
rust-${RUST_VERSION}-x86_64-unknown-linux-gnu.tar.gz  
#-------------------------------------------------------------------------------  
################################################################################  
  
  
  
## GOLANG
######################################################################  
#-------------------------------------------------------------------------------  
ENV GOLANG_VERSION 1.7.1  
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
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
nodejs  
#...............................................................................  
# Flask  
COPY requirements_flask.txt requirements_flask.txt  
RUN pip install -r requirements_flask.txt  
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
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/requirements_*.txt \  
/install_*.sh  
#-------------------------------------------------------------------------------  
# Script to setup git  
COPY scripts/start.sh /usr/local/bin/start.sh  
#-------------------------------------------------------------------------------  
# Create a user to run things as  
# - Set username to be created (default 'docker')  
ARG USERNAME=docker  
ENV USERNAME docker  
  
RUN useradd -m -s /bin/bash -U -G users ${USERNAME} && echo "${USERNAME}
ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/users  
  
ENV LANG en_US.utf8  
USER ${USERNAME}  
  
COPY scripts/ereduce /home/${USERNAME}/bin/ereduce  
COPY scripts/emonitor /home/${USERNAME}/bin/emonitor  
COPY scripts/eGSA /home/${USERNAME}/bin/eGSA  
COPY scripts/ispec /home/${USERNAME}/bin/ispec  
  
# Vim setup for the user  
RUN cd /home/${USERNAME}/ && \  
mkdir -p .vim/undodir/ && \  
mkdir -p .vim/spell/ && \  
mkdir -p .vim/autoload/ && \  
cd /home/${USERNAME}/.vim/autoload && \  
wget --quiet https://raw.githubusercontent.com/junegunn/vim-
plug/master/plug.vim && \  
cd /home/${USERNAME}/ && \  
wget --quiet https://raw.githubusercontent.com/marblestation/vim-complex-
sensible/master/vimrc -O .vim/vimrc && \  
ln -s .vim/vimrc .vimrc && \  
cd /home/${USERNAME}/.vim/spell/ && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/en.utf-8.spl && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/en.utf-8.sug && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/es.utf-8.spl && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/es.utf-8.sug && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/fr.utf-8.spl && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/fr.utf-8.sug && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/ca.utf-8.spl && \  
wget --quiet http://ftp.vim.org/vim/runtime/spell/ca.utf-8.sug && \  
cd /home/${USERNAME}/ && \  
vim +PlugInstall +qall  
  
COPY configurations/tmux.conf /home/${USERNAME}/.tmux.conf  
COPY configurations/bash_profile /home/${USERNAME}/.bash_profile  
RUN cd /home/${USERNAME}/ && \  
echo "source \$HOME/.bash_profile" >> /home/${USERNAME}/.bashrc && \  
git clone https://github.com/magicmonty/bash-git-prompt.git
/home/${USERNAME}/.bash-git-prompt --depth=1 && \  
sudo chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}/  
  
  
WORKDIR /home/${USERNAME}/  
ENTRYPOINT ["tini", "--"]  
cmd ["/usr/local/bin/start.sh"]  
################################################################################  


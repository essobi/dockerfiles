FROM debian:stretch  
LABEL maintainer="liang-bo.wang@wustl.edu"  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Upgrade APT  
# Configure locale and timezone  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends apt-utils && \  
echo "America/Chicago" > /etc/timezone && \  
rm /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata; \  
apt-get update && apt-get install -y locales && \  
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure -f noninteractive locales && \  
/usr/sbin/update-locale LANG=en_US.UTF-8; \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV LANG="en_US.UTF-8" LANGUAGE="en_US:en" LC_ALL="en_US.UTF-8" \  
PATH="/opt/conda/bin:${PATH}"  
  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends \  
tmux less libreadline7 gzip bzip2 gnupg2 \  
openssh-client wget curl ca-certificates rsync \  
libglib2.0-0 libxext6 libsm6 libxrender1 git vim-nox make \  
htop parallel ncdu \  
libnss-sss && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Fish shell  
RUN wget -nv
http://download.opensuse.org/repositories/shells:fish:release:2/Debian_9.0/Release.key
-O Release.key && \  
apt-key add Release.key && \  
echo 'deb
http://download.opensuse.org/repositories/shells:/fish:/release:/2/Debian_9.0/
/' > /etc/apt/sources.list.d/fish.list && \  
apt-get update && \  
apt-get install -y \--no-install-recommends fish && \  
chsh -s /usr/bin/fish && \  
rm Release.key && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Miniconda3  
RUN wget \--quiet
https://repo.continuum.io/miniconda/Miniconda3-4.5.1-Linux-x86_64.sh -O
$HOME/miniconda.sh && \  
/bin/bash $HOME/miniconda.sh -b -p /opt/conda && \  
conda config \--add channels conda-forge && \  
conda config \--add channels bioconda && \  
echo '. /opt/conda/etc/profile.d/conda.sh' > /etc/profile.d/conda.sh && \  
rm $HOME/miniconda.sh  
  
# Fish shell setting  
RUN git clone https://github.com/ccwang002/dotfiles.git $HOME/dotfiles && \  
cd $HOME/dotfiles && \  
/opt/conda/bin/python3 ./dotfile_setup.py \  
\--only "~/.inputrc" \--only "~/.editrc" \--only "~/.tmux.conf" && \  
rm -rf /root/.cache  
# Ripgrep, exa, and fd  
RUN wget \--quiet
https://github.com/BurntSushi/ripgrep/releases/download/0.8.1/ripgrep-0.8.1-x86_64-unknown-
linux-musl.tar.gz -O $HOME/ripgrep.tar.gz && \  
cd $HOME && tar xf $HOME/ripgrep.tar.gz && \  
cd `find $HOME -type d -name "ripgrep*"` && \  
mkdir -p /usr/local/share/man/man1 && \  
cp doc/rg.1 /usr/local/share/man/man1/ && \  
cp rg /usr/local/bin/ && \  
cp complete/rg.fish /usr/share/fish/vendor_completions.d && \  
rm -rf $HOME/ripgrep* && \  
\  
wget \--quiet
https://storage.googleapis.com/dinglab/lbwang/tools/exa/v0.8.0_linux_musl/exa
-O /usr/local/bin/exa && \  
wget \--quiet
https://storage.googleapis.com/dinglab/lbwang/tools/exa/v0.8.0_linux_musl/exa.1
-O /usr/local/share/man/man1/exa.1 && \  
wget \--quiet
https://storage.googleapis.com/dinglab/lbwang/tools/exa/v0.8.0_linux_musl/completions.fish
-O /usr/share/fish/vendor_completions.d/exa.fish && \  
chmod 755 /usr/local/bin/exa && \  
\  
wget \--quiet
https://github.com/sharkdp/fd/releases/download/v7.0.0/fd-v7.0.0-x86_64-unknown-
linux-musl.tar.gz -O $HOME/fd.tar.gz && \  
cd $HOME && tar xf $HOME/fd.tar.gz && \  
cd `find $HOME -type d -name "fd*"` && \  
cp fd /usr/local/bin/ && \  
cp autocomplete/fd.fish /usr/share/fish/vendor_completions.d/ && \  
cp fd.1 /usr/local/share/man/man1/ && \  
rm -rf $HOME/fd*  


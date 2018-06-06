  
FROM ubuntu:16.04  
  
MAINTAINER Wenbin Hou <catchyrime@fastmail.com>  
  
SHELL [ "/bin/bash", "-c" ]  
  
ARG LOCALE="en_US.UTF-8"  
  
  
ENV DEBIAN_FRONTEND="noninteractive"  
RUN set -x -e; \  
apt-get \--yes --quiet update; \  
apt-get \--yes --quiet dist-upgrade; \  
apt-get \--yes --quiet install apt-utils; \  
\  
apt-get \--yes --quiet install locales; \  
locale-gen "$LOCALE"; \  
dpkg-reconfigure locales; \  
export LC_ALL="$LOCALE"; \  
export LANG="$LOCALE"; \  
export LANGUAGE="$LOCALE"; \  
\  
apt-get \--yes --quiet install \  
apt-transport-https bash-completion curl dstat \  
less net-tools \  
software-properties-common sudo unzip vim vim-doc wget xzip xz-utils; \  
\  
add-apt-repository --yes --update ppa:git-core/ppa; \  
curl -s "https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh" | bash; \  
apt-get \--yes --quiet install git git-lfs; \  
git lfs install; \  
\  
apt-get \--yes --quiet autoclean; \  
rm -rf "/var/lib/apt/lists/*"  
  
COPY .bashrc /root/.bashrc  
COPY .vimrc /root/.vimrc  
COPY .inputrc /root/.inputrc  
COPY vimrc /etc/vim/vimrc  
  
  
ENV LC_ALL="$LOCALE"  
ENV LANG="$LOCALE"  
ENV LANGUAGE="$LOCALE"  
  
WORKDIR /root  
  
  


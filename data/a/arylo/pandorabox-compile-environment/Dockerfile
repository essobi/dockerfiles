FROM ubuntu:14.04  
MAINTAINER Arylo Yeung <arylo.open@gmail.com>  
  
LABEL \  
UPDATE_DATE=2016-06-30  
  
ENV \  
LIB_PATH=/work  
  
ARG REPO_URL=archive.ubuntu.com  
ARG SCRIPT_URL=https://raw.githubusercontent.com/PandoraboxTeam/Compile-
Environment/master/ubuntu.sh  
  
ARG USER=PandoraBox  
ARG GROUP=PandoraBox  
ARG UID=1000  
ARG GID=1000  
# Set Local  
RUN \  
locale-gen en_US.UTF-8 && \  
update-locale \  
LANG="en_US.UTF-8" \  
LANGUAGE="en_US:en" \  
LC_CTYPE="en_US.UTF-8" \  
LC_NUMERIC="en_US.UTF-8" \  
LC_TIME="en_US.UTF-8" \  
LC_COLLATE="en_US.UTF-8" \  
LC_MONETARY="en_US.UTF-8" \  
LC_MESSAGES="en_US.UTF-8" \  
LC_PAPER="en_US.UTF-8" \  
LC_NAME="en_US.UTF-8" \  
LC_ADDRESS="en_US.UTF-8" \  
LC_TELEPHONE="en_US.UTF-8" \  
LC_MEASUREMENT="en_US.UTF-8" \  
LC_IDENTIFICATION="en_US.UTF-8"  
  
# Run automated install script  
RUN \  
echo "[PandoraBox] Use APT URL" && \  
sed -i "s/archive.ubuntu.com/${REPO_URL}/g" /etc/apt/sources.list && \  
echo "[PandoraBox] Updating APT list" && \  
apt-get update -qq && \  
echo "[PandoraBox] Downloading curl from APT" && \  
apt-get install -y curl > /dev/null && \  
echo "[PandoraBox] Downloading script file from ${SCRIPT_URL}" && \  
curl -sL $SCRIPT_URL | bash > /dev/null  
  
# Clear cache  
RUN \  
apt-get clean && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /tmp/*  
  
RUN \  
mkdir -p $LIB_PATH && \  
mkdir -p /home/${USER}  
  
RUN groupadd -g ${GID} ${GROUP} && \  
useradd -d "/home/${USER}" -u ${UID} -g ${GID} -m -s /bin/bash ${USER} && \  
chown ${USER}:${USER} /home/${USER}  
USER ${USER}  
  
VOLUME ["${LIB_PATH}"]  
  
WORKDIR /home/${USER}  


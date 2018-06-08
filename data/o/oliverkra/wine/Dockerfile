FROM ubuntu:zesty  
  
ENV _USER=ubuntu  
ENV _GROUP=ubuntu  
ENV _UID=1000  
ENV _GID=1000  
RUN DEBIAN_FRONTEND=noninteractive && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends software-properties-common wget
apt-transport-https && \  
dpkg --add-architecture i386 && \  
wget https://dl.winehq.org/wine-builds/Release.key && \  
apt-key add Release.key && \  
apt-add-repository 'https://dl.winehq.org/wine-builds/ubuntu/' && \  
apt-get update && \  
apt-get install -y --install-recommends winehq-devel sudo && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /home/${_USER} && \  
mkdir -p /home/${_USER}/.wine && \  
echo "${_USER}:x:${_UID}:${_GID}:${_GROUP},,,:/home/${_USER}:/bin/bash" >>
/etc/passwd && \  
echo "${_GROUP}:x:${_UID}:" >> /etc/group && \  
echo "${_USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${_USER} && \  
chmod 0440 /etc/sudoers.d/${_USER} && \  
chown ${_USER}:${_GROUP} -R /home/${_USER}  
  
USER ${_USER}  
ENV HOME /home/${_USER}  
WORKDIR $HOME  
  
COPY highdpi.reg $HOME/highdpi.reg  
# RUN regedit $HOME/highdpi.reg


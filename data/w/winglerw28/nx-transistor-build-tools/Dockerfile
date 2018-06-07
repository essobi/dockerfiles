FROM greyltc/archlinux:2018-04-23  
# Ensure that libnx and libtransistor have the proper ENV variables set so
that you don't need to specify them every time.  
ENV DEVKITPRO=/opt/devkitpro \  
DEVKITARM=/opt/devkitpro/devkitARM \  
DEVKITPPC=/opt/devkitpro/devkitPPC \  
GPG_KEYSERVER="hkp://ipv4.pool.sks-keyservers.net:11371" \  
LIBTRANSISTOR_HOME=/opt/libtransistor \  
LIBTRANSISTOR_VER=1.2.3 \  
REQUIRED_PACKAGES=" \  
base-devel \  
clang \  
cmake \  
devkitARM \  
git \  
lld \  
llvm \  
python \  
python-pip \  
switch-dev" \  
REQUIRED_PIP_PACKAGES=" \  
pyelftools \  
lz4"  
# Set up Pacman with the keys to download devkitPro, then install the Switch
development tools for libnx.  
RUN pacman-key --recv F7FD5492264BB9D0; \  
pacman-key --lsign F7FD5492264BB9D0; \  
echo "[dkp-libs]" >> /etc/pacman.conf; \  
echo "Server = http://downloads.devkitpro.org/packages" >> /etc/pacman.conf; \  
echo "[dkp-linux]" >> /etc/pacman.conf; \  
echo "Server = http://downloads.devkitpro.org/packages/linux" >>
/etc/pacman.conf; \  
pacman -U "https://downloads.devkitpro.org/devkitpro-
keyring-r1.787e015-2-any.pkg.tar.xz" \--noconfirm; \  
pacman -Syu $REQUIRED_PACKAGES --noconfirm; \  
#  
# Download libtransistor's binary release and extract it to the proper
location.  
curl -OL
https://github.com/reswitched/libtransistor/releases/download/v$LIBTRANSISTOR_VER/libtransistor_v$LIBTRANSISTOR_VER.tar.gz;
\  
mkdir -p $LIBTRANSISTOR_HOME; \  
tar -C $LIBTRANSISTOR_HOME -xvzf libtransistor_v$LIBTRANSISTOR_VER.tar.gz ./;
\  
rm -f libtransistor_v$LIBTRANSISTOR_VER.tar.gz; \  
#  
# Update pip and install the dependencies required by libtransistor.  
pip install --upgrade pip; \  
pip install $REQUIRED_PIP_PACKAGES;  
  
ENTRYPOINT [ "/bin/bash", "-c" ]  
CMD [ "'echo \"You must provide a command to run to the Docker image!\"'" ]  


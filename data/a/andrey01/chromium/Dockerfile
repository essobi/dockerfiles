FROM ubuntu:zesty  
MAINTAINER Andrey Arapov <andrey.arapov@nixaid.com>  
  
# To avoid problems with Dialog and curses wizards  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install ca-certificates sudo kmod attr \  
pulseaudio libcanberra-gtk-module libexif12 \  
fonts-dejavu-core fonts-freefont-ttf fonts-guru-extra \  
fonts-kacst fonts-kacst-one fonts-khmeros-core fonts-lao \  
fonts-liberation fonts-lklug-sinhala fonts-lohit-guru \  
fonts-nanum fonts-opensymbol fonts-sil-abyssinica \  
fonts-sil-padauk fonts-symbola fonts-takao-pgothic \  
fonts-tibetan-machine fonts-tlwg-garuda-ttf \  
fonts-tlwg-kinnari-ttf fonts-tlwg-laksaman-ttf \  
fonts-tlwg-loma-ttf fonts-tlwg-mono-ttf \  
fonts-tlwg-norasi-ttf fonts-tlwg-purisa-ttf \  
fonts-tlwg-sawasdee-ttf fonts-tlwg-typewriter-ttf \  
fonts-tlwg-typist-ttf fonts-tlwg-typo-ttf \  
fonts-tlwg-umpush-ttf fonts-tlwg-waree-ttf \  
ttf-bitstream-vera ttf-dejavu-core ttf-ubuntu-font-family \  
fonts-arphic-ukai fonts-arphic-uming \  
fonts-ipafont-mincho fonts-ipafont-gothic \  
fonts-unfonts-core fonts-telu fonts-knda \  
chromium-browser && \  
rm -rf -- /var/lib/apt/lists  
  
# Obtain Google Chrome  
ADD https://dl.google.com/linux/direct/google-talkplugin_current_amd64.deb
/tmp/google-talkplugin_current_amd64.deb  
  
RUN sh -c 'dpkg -i /tmp/google-talkplugin_current_amd64.deb 2>/dev/null; exit
0' && \  
apt-get update && \  
apt-get -fy --no-install-recommends install && \  
rm -rf -- /var/lib/apt/lists /tmp/*.deb  
  
# Workaround: pulseaudio client library likes to remove /dev/shm/pulse-shm-*  
# files created by the host, causing sound to stop working.  
# To fix this, we either want to disable the shm or mount /dev/shm  
# in read-only mode when starting the container.  
RUN echo "enable-shm = no" >> /etc/pulse/client.conf  
  
ENV USER user  
ENV GROUPS video,audio  
ENV UID 1000  
ENV HOME /home/$USER  
RUN useradd -u $UID -m -d $HOME -s /usr/sbin/nologin -G $GROUPS $USER && \  
su -s /bin/sh -l $USER -c 'mkdir -p $HOME/.pki/nssdb $HOME/.local'  
  
RUN echo "$USER ALL=NOPASSWD:/sbin/lsmod" | tee /etc/sudoers.d/$USER && \  
/bin/echo -e "#!/bin/sh\nsudo /sbin/lsmod \$@" | tee /usr/local/sbin/lsmod &&
\  
chmod +x /usr/local/sbin/lsmod  
  
WORKDIR $HOME  
  
COPY launch /launch  
ENTRYPOINT [ "sh", "/launch" ]  


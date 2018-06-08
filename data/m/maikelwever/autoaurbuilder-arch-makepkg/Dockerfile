FROM logankoester/archlinux  
MAINTAINER Maikel Wever <maikelwever@gmail.com>  
  
# Adding mirrorlist with Dutch servers for when I build locally  
# Doesn't matter much on Docker Hub  
ADD mirrorlist /etc/pacman.d/mirrorlist  
  
RUN echo "[multilib]" >> /etc/pacman.conf \  
&& echo "Include = /etc/pacman.d/mirrorlist" >> /etc/pacman.conf \  
&& sed -i -e 's/#IgnorePkg =/IgnorePkg = sudo/' /etc/pacman.conf  
  
RUN pacman -Sy --noconfirm && \  
pacman -S archlinux-keyring --noconfirm && \  
pacman -Su --noconfirm && \  
pacman -S --needed --noconfirm base-devel && \  
echo -ne '\ny\ny\ny\ny\n' | pacman --needed -S multilib-devel && \  
pacman -Scc --noconfirm  
  
RUN curl -o /tmp/sudo-1.8.14.p3-2-x86_64.pkg.tar.xz -L
http://seblu.net/a/archive/packages/s/sudo/sudo-1.8.14.p3-2-x86_64.pkg.tar.xz
&& \  
pacman -U --force /tmp/sudo-1.8.14.p3-2-x86_64.pkg.tar.xz --noconfirm  
  
VOLUME /build  
WORKDIR /build  
  
ADD sudoers /etc/sudoers  
# Set up user & sudo  
RUN useradd -d /build -G wheel build && \  
chmod 0400 /etc/sudoers  
  
# Copy over buildscript  
ADD buildscript.sh /opt/buildscript.sh  
  
USER build  
  
# Options: Install dependencies, force package build, clean afterwards  
ENTRYPOINT sudo chown build: /build && \  
bash /opt/buildscript.sh  


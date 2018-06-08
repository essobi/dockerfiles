FROM archimg/base-devel  
  
LABEL maintainer="UPF"  
  
ARG MIRROR_URL="https://mirror.nl.leaseweb.net/archlinux/\$repo/os/\$arch"  
ARG REPO_URL="http://upf.space"  
ARG KEY_SERV="hkps://hkps.pool.sks-keyservers.net"  
ENV PACKAGER="UPF Docker Container <vic@demuzere.be>" \  
USER_ID="1000" \  
GROUP_ID="1000"  
# We'll need access to UPF repository.  
RUN pacman-key --keyserver "${KEY_SERV}" -r 6690CF94 && \  
pacman-key --lsign 6690CF94 && \  
pacman-key --keyserver "${KEY_SERV}" -r 455BE60E && \  
pacman-key --lsign 455BE60E && \  
pacman-key --keyserver "${KEY_SERV}" -r CF1F8674 && \  
pacman-key --lsign CF1F8674 && \  
echo -e "\n[multilib]\nInclude = /etc/pacman.d/mirrorlist\n\n[upf]\nSigLevel =
PackageRequired\nServer = ${REPO_URL}/\$arch\n\n[upf-any]\nSigLevel =
PackageRequired\nServer=${REPO_URL}/any" >> /etc/pacman.conf && \  
echo "Server = ${MIRROR_URL}" > /etc/pacman.d/mirrorlist && \  
groupadd -g "${GROUP_ID}" packager && \  
useradd -u "${USER_ID}" -g "${GROUP_ID}" -m packager && \  
echo "packager ALL=(ALL) NOPASSWD: /usr/bin/pacman" > /etc/sudoers.d/packager  
  
WORKDIR /home/packager  
  
COPY package.sh /opt  
  
CMD [ "/bin/sh", "-c", "/opt/package.sh" ]  


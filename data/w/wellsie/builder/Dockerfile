FROM debian:jessie  
MAINTAINER jono <jono@bowerswilkins.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN set -eux &&\  
apt-get update &&\  
apt-get upgrade -y &&\  
apt-get install -yq \  
apt-utils bash bc binutils binutils-gold build-essential bzip2 \  
chrpath cpio curl curl debianutils diffstat doxygen flex \  
g++ gawk gawk gcc gcc-multilib gettext git git-core \  
libc6-dev libc6-dev-i386 libncurses5-dev libncurses5-dev libpcre3-dev libssl-
dev \  
libxml-parser-perl locales lzop make man ocaml ocaml-findlib ocaml-nox ocaml-
nox \  
patch pkg-config python python-yaml python3 python3-pexpect python3-pip quilt
\  
screen sharutils socat subversion sudo texinfo unzip unzip vim wget xz-utils
zlib1g-dev &&\  
rm -rf /var/lib/apt-lists/* &&\  
echo "dash dash/sh boolean false" | debconf-set-selections &&\  
dpkg-reconfigure dash &&\  
echo "build ALL=(ALL) NOPASSWD: ALL" | tee -a /etc/sudoers &&\  
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen &&\  
curl http://storage.googleapis.com/git-repo-downloads/repo >
/usr/local/bin/repo &&\  
chmod a+x /usr/local/bin/repo  
  
ENV LANG en_US.utf8  
  
WORKDIR /src  
  
CMD [ "/bin/bash" ]  


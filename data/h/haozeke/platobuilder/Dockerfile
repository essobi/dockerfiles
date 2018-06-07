# Use the the recommended version [from
https://github.com/baskerville/plato/blob/master/doc/BUILD.md]  
FROM ubuntu:precise  
  
# By Rohit Goswami  
LABEL maintainer="Rohit Goswami <rohit.1995@mail.ru>"  
LABEL name="platoBot"  
  
# Suppress debconf errors [from https://github.com/phusion/baseimage-
docker/issues/58]  
ENV DEBIAN_FRONTEND noninteractive  
  
# Suppress policy restart errors [from https://forums.docker.com/t/error-in-
docker-image-creation-invoke-rc-d-policy-rc-d-denied-execution-of-restart-
start/880]  
RUN echo exit 0 > /usr/sbin/policy-rc.d  
  
# Add a clean step to every run [from https://medium.com/unbabel-dev/the-need-
for-speed-optimizing-dockerfiles-at-unbabel-70102f6d6745]  
# The clean step is from Phusion  
# Grab faster mirrors [from https://linuxconfig.org/how-to-select-the-fastest-
apt-mirror-on-ubuntu-linux]  
RUN apt-get update && apt-get install --yes wget; \  
wget
http://ftp.au.debian.org/debian/pool/main/n/netselect/netselect_0.3.ds1-26_amd64.deb;
\  
dpkg -i netselect_0.3.ds1-26_amd64.deb; \  
rm -rf netselect_*; \  
netselect -s 20 -t 40 $(wget -qO - mirrors.ubuntu.com/mirrors.txt); \  
sed -i
's/http:\/\/us.archive.ubuntu.com\/ubuntu\//http:\/\/ubuntu.uberglobalmirror.com\/archive\//'
/etc/apt/sources.list; apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
# Update apt and get build reqs [from https://github.com/koreader/koreader]  
RUN apt-get update && apt-get install --yes \  
curl libtool automake cmake ragel \  
zlib1g-dev libjpeg8-dev libjbig2dec0-dev \  
gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf \  
# Additional build deps  
texinfo libtool m4 build-essential \  
gettext ccache git sudo pkg-config; \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Horrible hack to get rustup [from https://github.com/rust-lang-
nursery/docker-rust/blob/master/1.26.1/jessie/Dockerfile]  
ENV RUSTUP_HOME=/usr/local/rustup \  
CARGO_HOME=/usr/local/cargo \  
PATH=/usr/local/cargo/bin:$PATH \  
RUST_VERSION=1.26.1  
RUN set -eux; \  
\  
# this "case" statement is generated via "update.sh"  
dpkgArch="$(dpkg --print-architecture)"; \  
case "${dpkgArch##*-}" in \  
amd64) rustArch='x86_64-unknown-linux-gnu';
rustupSha256='c9837990bce0faab4f6f52604311a19bb8d2cde989bea6a7b605c8e526db6f02'
;; \  
armhf) rustArch='armv7-unknown-linux-gnueabihf';
rustupSha256='297661e121048db3906f8c964999f765b4f6848632c0c2cfb6a1e93d99440732'
;; \  
arm64) rustArch='aarch64-unknown-linux-gnu';
rustupSha256='a68ac2d400409f485cb22756f0b3217b95449884e1ea6fd9b70522b3c0a929b2'
;; \  
i386) rustArch='i686-unknown-linux-gnu';
rustupSha256='27e6109c7b537b92a6c2d45ac941d959606ca26ec501d86085d651892a55d849'
;; \  
*) echo >&2 "unsupported architecture: ${dpkgArch}"; exit 1 ;; \  
esac; \  
\  
url="https://static.rust-lang.org/rustup/archive/1.11.0/${rustArch}/rustup-
init"; \  
wget "$url"; \  
echo "${rustupSha256} *rustup-init" | sha256sum -c -; \  
chmod +x rustup-init; \  
./rustup-init -y --no-modify-path --default-toolchain $RUST_VERSION; \  
rm rustup-init; \  
chmod -R a+w $RUSTUP_HOME $CARGO_HOME; \  
rustup --version; \  
cargo --version; \  
rustc --version;  
  
# Add the build user, update password to build and add to sudo group  
ENV USER build  
RUN useradd --create-home ${USER} && echo "${USER}:${USER}" | chpasswd &&
adduser ${USER} sudo  
  
# Switch to the new user by default and make ~/ the working dir  
WORKDIR /home/${USER}/  
  
# ccache specifics [https://github.com/stucki/docker-lineageos]  
ENV \  
CCACHE_SIZE=50G \  
CCACHE_DIR=$HOME/.ccache \  
USE_CCACHE=1 \  
CCACHE_COMPRESS=1  
# Use the shared volume for ccache storage  
ENV CCACHE_DIR /home/build/.ccache  
RUN ccache -M 50G  
  
# Fix permissions on home  
RUN sudo chown -R ${USER}:${USER} /home/${USER}  
  
USER ${USER}  
  
# Switch back to interactive shells  
ENV DEBIAN_FRONTEND teletype  
  
# Switch to bash  
SHELL ["/bin/bash", "-c"]  
  
# Setup dummy git config  
RUN git config --global user.name "${USER}" && git config --global user.email
"${USER}@localhost"  
  
# Get a transfer.sh macro  
RUN echo $'transfer() { if [ $# -eq 0 ]; then echo -e "No arguments specified.
Usage:\necho transfer /tmp/test.md\ncat /tmp/test.md | transfer test.md";
return 1; fi' >> ~/.bashrc && \  
echo $'tmpfile=$( mktemp -t transferXXX ); if tty -s; then basefile=$(basename
"$1" | sed -e 's/[^a-zA-Z0-9._-]/-/g'); curl --progress-bar --upload-file "$1"
"https://transfer.sh/$basefile" >> $tmpfile; else curl --progress-bar
--upload-file "-" "https://transfer.sh/$1" >> $tmpfile ; fi; cat $tmpfile; rm
-f $tmpfile; } ' >> ~/.bashrc  
  
# Get rust (from https://github.com/rust-lang-deprecated/rustup.sh/issues/83)  
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y  
  
# Get tool-chains  
RUN rustup target add arm-unknown-linux-gnueabihf  
  
# Setup cargo  
RUN mkdir -p ~/.cargo && touch ~/.cargo/config; \  
echo $'[target.arm-unknown-linux-gnueabihf]\nlinker = "arm-linux-gnueabihf-
gcc"\nrustflags = ["-C", "target-feature=+v7,+vfp3,+a9,+neon"]' >>
~/.cargo/config  


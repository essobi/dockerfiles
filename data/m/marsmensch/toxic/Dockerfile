#  
# Dockerfile for toxic client  
# usage: docker run marsmensch/toxic  
#  
# Beertips welcome! BTC 1PboFDkBsW2i968UnehWwcSrM9Djq5LcLB  
# ▄▄▄█████▓ ▒█████ ▒██ ██▒ ██▓ ▄████▄  
# ▓ ██▒ ▓▒▒██▒ ██▒▒▒ █ █ ▒░▓██▒▒██▀ ▀█  
# ▒ ▓██░ ▒░▒██░ ██▒░░ █ ░▒██▒▒▓█ ▄  
# ░ ▓██▓ ░ ▒██ ██░ ░ █ █ ▒ ░██░▒▓▓▄ ▄██▒  
# ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒░██░▒ ▓███▀ ░  
# ▒ ░░ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓ ░ ░▒ ▒ ░  
# ░ ░ ▒ ▒░ ░░ ░▒ ░ ▒ ░ ░ ▒  
# ░ ░ ░ ░ ▒ ░ ░ ▒ ░░  
# ░ ░ ░ ░ ░ ░ ░  
#  
  
FROM ubuntu:16.04  
MAINTAINER Florian Maier <contact@marsmenschen.com>  
  
ENV TOXIC_GIT_URL git://github.com/JFreegman/toxic.git  
ENV TOXC_GIT_URL git://github.com/irungentoo/toxcore.git  
ENV REFRESHED_AT 2016-06-26  
  
############################  
# configuration variables  
############################  
# X11 support  
ENV DISABLE_X11=1  
# audio call support  
ENV DISABLE_AV=1  
# sound notifications  
ENV DISABLE_SOUND_NOTIFY=1  
# desktop notifications  
ENV DISABLE_DESKTOP_NOTIFY=1  
  
# install dependencies  
RUN apt-get autoclean && apt-get autoremove && apt-get update && \  
apt-get -qqy install --no-install-recommends build-essential \  
automake lib32ncursesw5-dev ncurses-dev libcurl4-openssl-dev \  
libopenal-dev libalut-dev libnotify-dev libopus-dev libvpx-dev \  
make autoconf libtool git libconfig-dev yasm libsodium18 \  
libsodium-dev libqrencode-dev wget autotools-dev check && \  
rm -rf /var/lib/apt/lists/*  
  
# toxcore & toxic  
RUN mkdir -p /opt/code/; cd /opt/code; git clone ${TOXC_GIT_URL} toxcore && \  
git clone ${TOXIC_GIT_URL} toxic && cd toxcore && autoreconf -i && \  
./configure && make && make install && cd ../toxic && make && make install &&
\  
ldconfig && rm -rf /opt/code/  
  
VOLUME ["/data"]  
  
# no parameters display help  
ENTRYPOINT ["/usr/local/bin/toxic"]  
CMD ["--help"]


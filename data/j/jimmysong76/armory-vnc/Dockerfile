FROM ubuntu:16.04  
MAINTAINER Jimmy Song <http://github.com/jimmysong>  
  
# Install LXDE, VNC server, Twisted, SWIG and Qt  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y lxde-core lxterminal
tightvncserver curl gnupg g++ libcrypto++-dev swig python-dev python-twisted
libqtcore4 libqt4-dev python-qt4 pyqt4-dev-tools python-psutil xdg-utils  
  
# Download bitcoin  
RUN mkdir /bitcoin  
WORKDIR /bitcoin  
ENV BITCOIN_VERSION 0.14.1  
RUN curl -SLO "https://bitcoin.org/bin/bitcoin-
core-${BITCOIN_VERSION}/bitcoin-${BITCOIN_VERSION}-x86_64-linux-gnu.tar.gz" \  
&& curl -SLO "https://bitcoin.org/bin/bitcoin-
core-${BITCOIN_VERSION}/SHA256SUMS.asc"  
  
# Verify and install download  
COPY laanwj-releases.asc /bitcoin  
RUN gpg --import laanwj-releases.asc \  
&& gpg --verify --trust-model=always SHA256SUMS.asc \  
&& gpg --decrypt --output SHA256SUMS SHA256SUMS.asc \  
&& grep "bitcoin-${BITCOIN_VERSION}-x86_64-linux-gnu.tar.gz" SHA256SUMS |
sha256sum -c - \  
&& tar -xzf "bitcoin-${BITCOIN_VERSION}-x86_64-linux-gnu.tar.gz" -C /usr
--strip-components=1 \  
&& rm "bitcoin-${BITCOIN_VERSION}-x86_64-linux-gnu.tar.gz" SHA256SUMS.asc
SHA256SUMS  
  
RUN ln -s /bitcoin /root/.bitcoin  
  
# Download armory  
RUN mkdir /armory  
WORKDIR /armory  
ENV ARMORY_VERSION 0.96  
RUN curl -SLO
"https://github.com/goatpig/BitcoinArmory/releases/download/v${ARMORY_VERSION}/armory_${ARMORY_VERSION}-gcc5.4_amd64.deb"  
RUN curl -SLO
"https://github.com/goatpig/BitcoinArmory/releases/download/v${ARMORY_VERSION}/sha256sum.txt.asc"  
  
# Verify and install download  
COPY goatpig-signing-key.asc /armory  
RUN gpg --import goatpig-signing-key.asc \  
&& gpg --verify --trust-model=always sha256sum.txt.asc \  
&& gpg --decrypt --output sha256sum.txt sha256sum.txt.asc \  
&& grep "armory_${ARMORY_VERSION}-gcc5.4_amd64.deb" sha256sum.txt | sha256sum
-c - \  
&& dpkg -i "armory_${ARMORY_VERSION}-gcc5.4_amd64.deb" \  
&& rm "armory_${ARMORY_VERSION}-gcc5.4_amd64.deb" sha256sum.txt.asc
sha256sum.txt  
  
RUN ln -s /armory /root/.armory  
  
# Set user for VNC server (USER is only for build)  
ENV USER root  
# Set default password  
COPY password.txt .  
RUN cat password.txt password.txt | vncpasswd \  
&& rm password.txt  
  
# Expose VNC port  
EXPOSE 5901  
# Copy VNC script that handles restarts  
COPY run.sh /opt/  
CMD ["/opt/run.sh"]  


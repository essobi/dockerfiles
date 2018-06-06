# Build Tor Browser Docker Image  
FROM debian:stable-slim  
MAINTAINER geoffh1977 <geoffh1977@gmail.com>  
  
# Set Variables For Docker Image  
ARG TOR_USER="user"  
ENV TOR_VERSION=""  
# Install Packages For Tor Browser and Firefox ESR  
RUN export DEBIAN_FRONTEND=noninteractive && \  
sed -i.bak 's/stable main/stable main contrib/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install --no-install-recommends -y curl xz-utils gpg dirmngr locales
ca-certificates firefox-esr && \  
apt-get clean autoclean && apt-get autoremove -y && rm -rf
/var/lib/{apt,dpkg,cache,log}/ && \  
localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 2> /dev/null || :  
  
# Add The User And Create The Directories  
RUN useradd -m -d /home/${TOR_USER} ${TOR_USER} && \  
mkdir -p /home/${TOR_USER}/Downloads /opt/tor /Downloads && \  
ln -s /Downloads /home/${TOR_USER}/Downloads && \  
chown ${TOR_USER}:${TOR_USER} -R /home/${TOR_USER} /opt/tor /Downloads  
  
# GPG Keys Loaded From File - Work Around For Unreliable GPG Key Server  
COPY assets/gnupg.tar.gz /tmp/gnupg.tar.gz  
COPY assets/VERSION /opt/tor/VERSION  
RUN mkdir -p /home/${TOR_USER}/.gnupg && \  
tar zxf /tmp/gnupg.tar.gz -C /home/${TOR_USER}/.gnupg --strip 1 && \  
chmod 700 /home/${TOR_USER}/.gnupg && \  
chown ${TOR_USER}:${TOR_USER} -R /home/${TOR_USER}/.gnupg && \  
rm -f /tmp/gnupg.tar.gz  
  
# Configure WorkDir And User  
WORKDIR /home/${TOR_USER}  
USER ${TOR_USER}  
  
# Download, Check, And Install Tor Project Files  
RUN cd /opt/tor && \  
export TOR_VERSION=$(cat /opt/tor/VERSION) && \  
curl -sSL -o /tmp/tor-browser-linux64-${TOR_VERSION}_en-US.tar.xz
https://www.torproject.org/dist/torbrowser/${TOR_VERSION}/tor-browser-
linux64-${TOR_VERSION}_en-US.tar.xz && \  
curl -sSL -o /tmp/tor-browser-linux64-${TOR_VERSION}_en-US.tar.xz.asc
https://www.torproject.org/dist/torbrowser/${TOR_VERSION}/tor-browser-
linux64-${TOR_VERSION}_en-US.tar.xz.asc && \  
# gpg --keyserver pool.sks-keyservers.net --recv-keys 0x4E2C6E8793298290 && \  
gpg --verify /tmp/tor-browser-linux64-${TOR_VERSION}_en-US.tar.xz.asc
/tmp/tor-browser-linux64-${TOR_VERSION}_en-US.tar.xz && \  
tar xf /tmp/tor-browser-linux64-${TOR_VERSION}_en-US.tar.xz && \  
rm -f /tmp/tor-browser-linux64-${TOR_VERSION}_en-US.tar.xz /tmp/tor-browser-
linux64-${TOR_VERSION}_en-US.tar.xz.asc /opt/tor/tor-browser_en-
US/Browser/Downloads && \  
ln -s /Downloads /opt/tor/tor-browser_en-US/Browser/Downloads  
  
VOLUME ["/Downloads"]  
  
# Set The Start Command  
CMD ["/opt/tor/tor-browser_en-US/Browser/start-tor-browser"]  


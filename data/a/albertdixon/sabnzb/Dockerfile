FROM alpine:3.5  
MAINTAINER Albert Dixon <albert@dixon.rocks>  
  
EXPOSE 8080 8090  
ENTRYPOINT ["/sbin/tini", "-g", "--"]  
CMD ["/bin/start"]  
ENV SABNZB_VERSION=1.2.0 \  
SIGIL_VERSION=0.4.0 \  
TINI_VERSION=v0.13.2 \  
  
PIA_REMOTE=nl.privateinternetaccess.com \  
PIA_REMOTE_PORT=1198 \  
VPN_AUTH=sha1 \  
VPN_CIPHER=aes-128-cbc \  
VPN_DEV=tun0 \  
VPN_PROTO=udp \  
VPN_VERBOSITY=1  
  
RUN apk add --update --no-cache --purge \  
autoconf \  
automake \  
ca-certificates \  
curl \  
g++ \  
gcc \  
libffi-dev \  
make \  
openssl \  
openssl-dev \  
openvpn \  
python \  
python-dev \  
p7zip \  
tar \  
tini \  
unrar \  
unzip \  
# Install par2cmdline  
&& curl -Ls -o par2.zip
https://github.com/Parchive/par2cmdline/archive/master.zip \  
&& unzip par2 \  
&& cd par2cmdline-master \  
&& aclocal && automake --add-missing && autoconf \  
&& ./configure && make && make install && cd .. \  
&& rm -rvf par2* \  
  
# Install python deps  
&& curl -s https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install -U pip \  
&& pip install -U --no-cache-dir \  
cheetah \  
pip \  
pyopenssl \  
supervisor \  
&& pip install http://www.golug.it/pub/yenc/yenc-0.4.0.tar.gz \  
  
# Install apps  
&& curl -Ls -o /sigil.tgz
https://github.com/gliderlabs/sigil/releases/download/v$SIGIL_VERSION/sigil_${SIGIL_VERSION}_Linux_x86_64.tgz
\  
&& curl -Ls -o /sabnzb.tgz
https://github.com/sabnzbd/sabnzbd/releases/download/$SABNZB_VERSION/SABnzbd-$SABNZB_VERSION-
src.tar.gz \  
&& mkdir -pv /usr/src/app \  
&& tar xvzf sigil.tgz -C /usr/local/bin \  
&& tar xvzf sabnzb.tgz --strip-components=1 -C /usr/src/app \  
&& rm -rvf *.tgz \  
# Clean up  
&& apk del --purge \  
gcc \  
autoconf \  
automake \  
git \  
g++ \  
make \  
python-dev \  
openssl-dev \  
libffi-dev \  
&& rm -rvf /var/cache/apk/* /tmp/* /var/tmp/*  
  
COPY start /bin/  
COPY config /config  


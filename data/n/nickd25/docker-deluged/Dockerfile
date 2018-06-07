FROM alpine:3.7  
MAINTAINER nickd25  
  
  
RUN apk update  
RUN apk upgrade  
  
# environment variables  
ENV PYTHON_EGG_CACHE="/config/plugins/.python-eggs"  
ENV PS1="$(whoami)@$(hostname):$(pwd)$ " \  
HOME="/root" \  
TERM="xterm"  
ARG Username="default"  
ARG Password="changeme69"  
ARG Puid="911"  
ARG Pgid="911"  
ENV USERNAME=$Username  
ENV PASSWORD=$Password  
ENV PGID=$Pgid  
ENV PUID=$Puid  
  
  
# s6 overlay  
RUN \  
echo "Install the s6 overlay" && \  
apk add --no-cache ca-certificates wget bash \  
&& wget https://github.com/just-
containers/s6-overlay/releases/download/v1.21.2.2/s6-overlay-amd64.tar.gz -O
/tmp/s6-overlay.tar.gz \  
&& tar xvfz /tmp/s6-overlay.tar.gz -C / \  
&& rm -f /tmp/s6-overlay.tar.gz  
  
RUN \  
echo "Build dependencies" && \  
apk add --no-cache --virtual=build-dependencies \  
curl \  
tar \  
g++ \  
gcc \  
libffi-dev \  
openssl-dev \  
py2-pip \  
python2-dev  
  
RUN \  
echo "Runtime Packages" && \  
apk add --no-cache \  
coreutils \  
shadow \  
tzdata \  
curl \  
libressl2.6-libssl \  
openssl \  
p7zip \  
unrar \  
unzip  
  
RUN \  
echo "Install deluge" && \  
apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/testing \  
deluge \  
geoip  
  
RUN \  
echo "**** install pip packages ****" && \  
pip install --no-cache-dir -U \  
incremental \  
crypto \  
mako \  
markupsafe \  
pyopenssl \  
service_identity \  
six \  
twisted \  
zope.interface  
  
RUN \  
echo "Clean up clean up everybody do your share." && \  
apk del --purge \  
build-dependencies && \  
rm -rf \  
/root/.cache  
  
RUN groupmod -g 1000 users \  
&& useradd -u 911 -U -d /config -s /bin/false abc \  
&& usermod -G users abc  
  
EXPOSE 58846 58946 58946/udp  
VOLUME /config /downloads  
  
# root filesystem  
COPY root /  
  
ENTRYPOINT [ "/init" ]


FROM ubuntu:16.04  
MAINTAINER Hunterhug <gdccmcm14@live.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed -i 's#http://archive.ubuntu.com/#http://cn.archive.ubuntu.com/#'
/etc/apt/sources.list  
  
# built-in packages  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends software-properties-common curl
\  
&& sh -c "echo 'deb
http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_16.04/ /' >>
/etc/apt/sources.list.d/arc-theme.list" \  
&& curl -SL
http://download.opensuse.org/repositories/home:Horst3180/xUbuntu_16.04/Release.key
| apt-key add - \  
# && add-apt-repository ppa:fcwu-tw/ppa \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends --allow-unauthenticated \  
supervisor \  
openssh-server pwgen \  
net-tools \  
lxde \  
x11vnc xvfb \  
gtk2-engines-murrine ttf-ubuntu-font-family \  
firefox \  
fonts-wqy-microhei \  
language-pack-zh-hant language-pack-gnome-zh-hant firefox-locale-zh-hant \  
nginx \  
python-pip python-dev build-essential \  
mesa-utils libgl1-mesa-dri \  
gnome-themes-standard gtk2-engines-pixbuf gtk2-engines-murrine pinta arc-theme
\  
dbus-x11 x11-utils  
  
ADD image /  
  
RUN pip install setuptools wheel && pip install -r
/usr/lib/web/requirements.txt  
  
# tini for subreap  
ENV TINI_VERSION v0.9.0  
ADD other/tini /bin/tini  
RUN chmod +x /bin/tini  
  
EXPOSE 80  
WORKDIR /root  
ENV HOME=/home/ubuntu \  
SHELL=/bin/bash  
  
########################################################################  
## other  
RUN apt-get install -y --no-install-recommends --allow-unauthenticated git vim
ttf-wqy-* xfonts-wqy fonts-wqy-* im-config  
RUN apt-get install -y --no-install-recommends --allow-unauthenticated fcitx
fcitx-googlepinyin  
RUN apt-get install -y --no-install-recommends --allow-unauthenticated fcitx-
config*  
RUN im-config -s fcitx  
  
########################################################################  
# golang1.8  
# gcc for cgo  
RUN apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
pkg-config \  
wget \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GOLANG_VERSION 1.8.3  
  
RUN set -eux; \  
\  
# this "case" statement is generated via "update.sh"  
dpkgArch="$(dpkg --print-architecture)"; \  
case "${dpkgArch##*-}" in \  
amd64) goRelArch='linux-amd64';
goRelSha256='1862f4c3d3907e59b04a757cfda0ea7aa9ef39274af99a784f5be843c80c6772'
;; \  
armhf) goRelArch='linux-armv6l';
goRelSha256='3c30a3e24736ca776fc6314e5092fb8584bd3a4a2c2fa7307ae779ba2735e668'
;; \  
i386) goRelArch='linux-386';
goRelSha256='ff4895eb68fb1daaec41c540602e8bb4c1e8bb2f0e7017367171913fc9995ed2'
;; \  
ppc64el) goRelArch='linux-ppc64le';
goRelSha256='e5fb00adfc7291e657f1f3d31c09e74890b5328e6f991a3f395ca72a8c4dc0b3'
;; \  
s390x) goRelArch='linux-s390x';
goRelSha256='e2ec3e7c293701b57ca1f32b37977ac9968f57b3df034f2cc2d531e80671e6c8'
;; \  
*) goRelArch='src'; goRelSha256='5f5dea2447e7dcfdc50fa6b94c512e58bfba5673c039259fd843f68829d99fa6'; \  
echo >&2; echo >&2 "warning: current architecture ($dpkgArch) does not have a
corresponding Go binary release; will be building from source"; echo >&2 ;; \  
esac; \  
\  
#url="https://golang.org/dl/go${GOLANG_VERSION}.${goRelArch}.tar.gz"; \  
url="https://www.golangtc.com/static/go/${GOLANG_VERSION}/go${GOLANG_VERSION}.${goRelArch}.tar.gz";
\  
wget -O go.tgz "$url"; \  
echo "${goRelSha256} *go.tgz" | sha256sum -c -; \  
tar -C /usr/local -xzf go.tgz; \  
rm go.tgz; \  
\  
if [ "$goRelArch" = 'src' ]; then \  
echo >&2; \  
echo >&2 'error: UNIMPLEMENTED'; \  
echo >&2 'TODO install golang-any from jessie-backports for GOROOT_BOOTSTRAP
(and uninstall after build)'; \  
echo >&2; \  
exit 1; \  
fi; \  
\  
export PATH="/usr/local/go/bin:$PATH"; \  
go version  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
  
COPY golang/go-wrapper /usr/local/bin/  
  
ENTRYPOINT ["/startup.sh"]  


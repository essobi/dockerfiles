FROM vcatechnology/raspbian-ci:zero  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Start emulation  
USER root  
RUN [ "cross-build-start" ]  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="An up-to-date Raspbian image with VCA tool chain
packages" \  
org.label-schema.url="https://www.raspbian.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-raspbian-
toolchain" \  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
# Install useful packages  
RUN vca-install-package \  
alsa-utils \  
automake \  
bc \  
bison \  
check \  
cmake \  
comerr-dev \  
cppcheck \  
dbus \  
debhelper \  
dfu-util \  
dialog \  
dnsmasq \  
dosfstools \  
doxygen \  
e2fslibs-dev \  
eject \  
flex \  
g++ \  
gawk \  
gcc \  
gdb \  
gdbserver \  
gdisk \  
gperf \  
graphviz \  
gsoap \  
gstreamer1.0-alsa \  
gstreamer1.0-libav \  
gstreamer1.0-plugins-bad \  
gstreamer1.0-plugins-good \  
gstreamer1.0-plugins-ugly \  
gstreamer1.0-tools \  
gstreamer1.0-vaapi \  
intltool \  
libaa-bin \  
libaa1-dev \  
libasm-dev \  
libasound2-dev \  
libasprintf-dev \  
libattr1-dev \  
libboost-all-dev \  
libbz2-dev \  
libcap-dev \  
libcap-ng-dev \  
libcppunit-dev \  
libcurl4-gnutls-dev \  
libdbus-1-dev \  
libdrm-dev \  
libdw-dev \  
libeigen3-dev \  
libelf-dev \  
libffi-dev \  
libgcrypt11-dev \  
libgettextpo-dev \  
libgmp-dev \  
libgnutls28-dev \  
libgpg-error-dev \  
libgsoap-dev \  
libgstreamer-plugins-bad1.0-dev \  
libgstreamer-plugins-base1.0-dev \  
libgstreamer1.0-dev \  
libgudev-1.0-dev \  
libicu-dev \  
libidn11-dev \  
libisl-dev \  
libjansson-dev \  
libkrad-dev \  
libkrb5-dev \  
libkeyutils-dev \  
libmount-dev \  
libmozjs185-dev \  
libmpc-dev \  
libmpfr-dev \  
libncurses5-dev \  
libncursesw5-dev \  
libndp-dev \  
libnl-3-dev \  
libnl-cli-3-dev \  
libnspr4-dev \  
libntlm0-dev \  
libopencv-dev \  
liborc-0.4-dev \  
libpam0g-dev \  
libpciaccess-dev \  
libpcre3-dev \  
libpng12-dev \  
libpolkit-agent-1-dev \  
libpolkit-gobject-1-dev \  
libpopt-dev \  
libprotobuf-dev \  
libprotoc-dev \  
libqt4-dev \  
libsigc++-2.0-dev \  
libsoup2.4-dev \  
libsqlite3-dev \  
libssl-dev \  
libsubunit-dev \  
libsystemd-dev \  
libtasn1-6-dev \  
libtinyxml-dev \  
libtool-bin \  
libudev-dev \  
libusb-1.0-0-dev \  
libva-dev \  
libverto-dev \  
libwebp-dev \  
libx264-dev \  
libxml2-dev \  
lintian \  
llvm \  
llvm-dev \  
make \  
mscgen \  
nasm \  
ncurses-term \  
nettle-dev \  
network-manager \  
nodejs \  
nodejs-legacy \  
npm \  
p7zip-full \  
pandoc \  
pkg-config \  
protobuf-compiler \  
python-pip \  
python-pystache \  
python-requests \  
python-tz \  
qemu \  
realpath \  
ss-dev \  
stress \  
subunit \  
unrar-free \  
uuid-runtime \  
vde2 \  
xzdec \  
yasm \  
zlib1g-dev  
  
RUN su build-server -c 'pip install --user cpplint sseclient
backports.functools_lru_cache coverage'  
  
RUN curl
http://ftp.us.debian.org/debian/pool/main/a/automake-1.15/automake_1.15-6_all.deb
> automake.deb \  
&& curl
http://ftp.us.debian.org/debian/pool/main/a/autoconf/autoconf_2.69-10_all.deb
> autoconf.deb \  
&& dpkg -i automake.deb autoconf.deb \  
&& rm autoconf.deb automake.deb \  
&& vca-install-package -f  
  
# Stop emulation  
RUN [ "cross-build-end" ]  
USER build-server  


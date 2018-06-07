FROM vcatechnology/fedora-ci:26  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Echo the PATH  
RUN echo "PATH=${PATH}"  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="An up-to-date Fedora image that has VCA tool
chain packages installed" \  
org.label-schema.url="https://getfedora.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-fedora-
toolchain" \  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
# Install useful packages  
RUN sudo vca-install-package \  
aalib \  
aalib-devel \  
alsa-lib-devel \  
alsa-utils \  
bc \  
bison \  
boost-devel \  
boost-static \  
bzip2-devel \  
check-devel \  
clang \  
clang-tools-extra \  
cmake \  
cppcheck \  
cppunit-devel \  
dbus-devel \  
dfu-util \  
dialog-devel \  
dnsmasq \  
dosfstools \  
doxygen \  
e2fsprogs \  
e2fsprogs-devel \  
eigen3-devel \  
elfutils-devel \  
elfutils-libelf-devel \  
flex \  
gcc \  
gcc-c++ \  
gdb \  
gdb-gdbserver \  
gdisk \  
gettext-devel \  
glib2-devel \  
glibc-nss-devel \  
gmp-devel \  
gnu-efi-devel \  
gnutls-devel \  
gperf \  
graphviz \  
gsoap-devel \  
gstreamer1-devel \  
gstreamer1-plugins-bad-free-devel \  
gstreamer1-plugins-base-devel \  
gstreamer1-plugins-good \  
gstreamer1-rtsp-server-devel \  
gstreamer1-vaapi \  
ilmbase-devel \  
intltool \  
iptables \  
isl-devel \  
jansson-devel \  
jasper-devel \  
js-devel \  
keyutils-libs-devel \  
libasan \  
libatomic \  
libattr-devel \  
libblkid-devel \  
libcap-devel \  
libcap-ng-devel \  
libcurl-devel \  
libffi-devel \  
libgcrypt-devel \  
libgpg-error-devel \  
libgudev-devel \  
libicu-devel \  
libidn-devel \  
libitm-devel \  
libjpeg-turbo-devel \  
libmount-devel \  
libmpc-devel \  
libndp-devel \  
libnl3-devel \  
libntlm-devel \  
libpciaccess-devel \  
libsigc++20-devel \  
libsoup-devel \  
libss-devel \  
libtiff-devel \  
libtool \  
libubsan \  
libusbx-devel \  
libuuid-devel \  
libuv-devel \  
libva-devel \  
libwebp-devel \  
libxml2-devel \  
llvm \  
llvm-devel \  
make \  
mpfr-devel \  
mscgen \  
nasm \  
ncurses-devel \  
ncurses-term \  
nettle-devel \  
NetworkManager \  
nodejs \  
npm \  
nspr-devel \  
opencv-devel \  
OpenEXR-devel \  
openssl-devel \  
openssl-static \  
orc-compiler \  
orc-devel \  
p7zip \  
pam-devel \  
pandoc \  
pcre-devel \  
pixman-devel \  
pkgconfig \  
polkit-devel \  
polkit \  
popt-devel \  
procps-ng \  
protobuf-devel \  
protobuf-lite-devel \  
pystache \  
python-devel \  
python-requests \  
pytz \  
qemu \  
qt-devel \  
rapidjson-devel \  
rapidxml-devel \  
rpm-build \  
rpmlint \  
sqlite-devel \  
stress \  
subunit-filters \  
systemd-devel \  
systemd-udev \  
tinyxml-devel \  
uuid \  
uuidd \  
valgrind \  
xz-devel \  
xz-lzma-compat \  
yasm \  
zlib-devel  
  
RUN pip install --user sseclient cpplint backports.functools_lru_cache
coverage  


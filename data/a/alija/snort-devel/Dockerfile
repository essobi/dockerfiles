FROM ubuntu:16.04  
  
MAINTAINER Alija Sabic <sabic.alija@gmail.com>  
  
# Partially based on  
# https://sublimerobots.com/2017/07/installing-snort-3-b237-in-ubuntu  
  
ARG UID  
ARG GID  
ARG USERNAME  
ARG GROUPNAME  
ARG DOWNLOAD_DIR  
ARG LOG_DIR  
ARG SNORT_INSTALL  
ARG SNORT_PROJECT  
ARG ECLIPSE_WORKSPACE  
  
# Setup Environment
-------------------------------------------------------------------------------------------------------/  
ENV UID=${UID:-1000} \  
GID=${GID:-1000} \  
USERNAME=${USERNAME:-developer} \  
GROUPNAME=${GROUPNAME:-Developer} \  
DOWNLOAD_DIR=${DOWNLOAD_DIR:-/home/temp} \  
LOG_DIR=${LOG_DIR:-/home/logs} \  
SNORT_INSTALL=${SNORT_INSTALL:-/opt/snort} \  
JAVA_HOME=/usr/lib/jvm/java-8-oracle \  
NO_AT_BRIDGE=1 \  
VER_ZLIB=1.2.11 \  
VER_PKGCFG=0.29.2 \  
VER_PCAP=1.8.1 \  
VER_PCRE=8.41 \  
VER_SSL=1.1.0g \  
VER_LUAJIT=2.0.5 \  
VER_HWLOC=1.11.8 \  
VER_SAFEC=10052013 \  
VER_BOOST=1.64.0 \  
DIR_BOOST=boost_1_64_0 \  
VER_RAGEL=6.10 \  
VER_HYPERSCAN=4.5.1 \  
VER_DAQ=2.2.2 \  
VER_SNORT=3.0.0 \  
VER_SNORT_EXTRA=1.0.0 \  
VER_SNORT_SUB=240 \  
TAG_SNORT=BUILD_240 \  
VER_ECLIPSE=oxygen/R/eclipse-cpp-oxygen-R-linux-gtk-x86_64  
  
ENV SNORT_PROJECT=${SNORT_PROJECT:-/home/${USERNAME}/snort-project} \  
ECLIPSE_WORKSPACE=${ECLIPSE_WORKSPACE:-/home/${USERNAME}/workspace} \  
LUA_PATH=${SNORT_INSTALL}/include/snort/lua/\?.lua\;\; \  
SNORT_LUA_PATH=${SNORT_INSTALL}/etc/snort \  
URL_ZLIB=www.zlib.net/zlib-${VER_ZLIB}.tar.gz \  
URL_PKGCFG=https://pkg-config.freedesktop.org/releases/pkg-
config-${VER_PKGCFG}.tar.gz \  
URL_PCAP=http://www.tcpdump.org/release/libpcap-${VER_PCAP}.tar.gz \  
URL_PCRE=ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${VER_PCRE}.tar.gz
\  
URL_SSL=https://www.openssl.org/source/openssl-${VER_SSL}.tar.gz \  
URL_LUAJIT=http://luajit.org/download/LuaJIT-${VER_LUAJIT}.tar.gz \  
URL_HWLOC=https://www.open-
mpi.org/software/hwloc/v1.11/downloads/hwloc-${VER_HWLOC}.tar.gz \  
URL_LIBDNET=https://github.com/jncornett/libdnet.git \  
URL_LIBDNET_ALT=https://github.com/dugsong/libdnet.git \  
URL_SAFEC=http://downloads.sourceforge.net/project/safeclib/libsafec-${VER_SAFEC}.tar.gz
\  
URL_BOOST=https://dl.bintray.com/boostorg/release/${VER_BOOST}/source/${DIR_BOOST}.tar.gz
\  
URL_RAGEL=http://www.colm.net/files/ragel/ragel-${VER_RAGEL}.tar.gz \  
URL_HYPERSCAN=https://github.com/01org/hyperscan/archive/v${VER_HYPERSCAN}.tar.gz
\  
URL_DAQ=https://www.snort.org/downloads/snortplus/daq-${VER_DAQ}.tar.gz \  
URL_SNORT=https://www.snort.org/downloads/snortplus/snort-${VER_SNORT}-cmake.tar.gz
\  
URL_SNORT_GIT=https://github.com/snortadmin/snort3.git \  
URL_SNORT_EXTRA=https://www.snort.org/downloads/snortplus/snort_extra-${VER_SNORT_EXTRA}-cmake.tar.gz
\  
URL_ECLIPSE=http://eclipse.mirror.rafal.ca/technology/epp/downloads/release/${VER_ECLIPSE}.tar.gz
\  
DIR_ZLIB=zlib-${VER_ZLIB} \  
DIR_PKGCFG=pkg-config-${VER_PKGCFG} \  
DIR_PCAP=libpcap-${VER_PCAP} \  
DIR_PCRE=pcre-${VER_PCRE} \  
DIR_SSL=openssl-${VER_SSL} \  
DIR_LUAJIT=LuaJIT-${VER_LUAJIT} \  
DIR_HWLOC=hwloc-${VER_HWLOC} \  
DIR_LIBDNET=libdnet \  
DIR_SAFEC=libsafec-${VER_SAFEC} \  
DIR_RAGEL=ragel-${VER_RAGEL} \  
DIR_HYPERSCAN=hyperscan-${VER_HYPERSCAN} \  
DIR_DAQ=daq-${VER_DAQ} \  
DIR_SNORT=snort-${VER_SNORT} \  
DIR_SNORT_GIT=snort3 \  
DIR_ECLIPSE=eclipse \  
LOG_ZLIB=zlib \  
LOG_PKGCFG=pkgcfg \  
LOG_PCAP=pcap \  
LOG_PCRE=pcre \  
LOG_SSL=openssl \  
LOG_LUAJIT=luajit \  
LOG_HWLOC=hwloc \  
LOG_LIBDNET=libdnet \  
LOG_SAFEC=safec \  
LOG_RAGEL=ragel \  
LOG_HYPERSCAN=hyperscan \  
LOG_DAQ=daq \  
LOG_SNORT=snort  
  
# Create user space  
RUN mkdir -p /home/${USERNAME} && \  
echo "${USERNAME}:x:${UID}:${GID}:${GROUPNAME},,,:/home/${USERNAME}:/bin/bash"
>> /etc/passwd && \  
echo "${USERNAME}:x:${UID}:" >> /etc/group && \  
mkdir -p /etc/sudoers.d && \  
echo "${USERNAME} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${USERNAME} && \  
chmod 0440 /etc/sudoers.d/${USERNAME} && \  
chown ${UID}:${GID} -R /home/${USERNAME} && \  
mkdir -p ${DOWNLOAD_DIR} && mkdir -p ${LOG_DIR}  
# Needed tools  
RUN apt-get update && apt-get install -y \  
software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && apt-get install -y \  
w3m \  
wget \  
gdb \  
nautilus \  
autoconf \  
autotools-dev \  
build-essential \  
cmake \  
git-core \  
bison \  
flex \  
python \  
libpcap-dev \  
libtool \  
liblzma-dev \  
libsqlite3-dev \  
cpputest \  
asciidoc \  
source-highlight \  
software-properties-common \  
oracle-java8-installer \  
dbus-x11 \  
packagekit-gtk3-module \  
libcanberra-gtk-module \  
libcanberra-gtk3-module && \  
apt-get autoremove -y && apt-get clean  
# dblatex \  
# Build & Install Snort Dependencies
--------------------------------------------------------------------------------------/  
WORKDIR ${DOWNLOAD_DIR}  
# Zlib  
RUN wget -qO- ${URL_ZLIB} | tar xz && \  
cd ${DIR_ZLIB} && \  
./configure | tee ${LOG_DIR}/${LOG_ZLIB}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_ZLIB}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_ZLIB}_make_install.log 2>&1 && \  
cd .. && rm -rf ${DIR_ZLIB}  
# PkgConfig  
RUN wget -qO- ${URL_PKGCFG} | tar xz && \  
cd ${DIR_PKGCFG} && \  
./configure --with-internal-glib | tee ${LOG_DIR}/${LOG_PKGCFG}_configure.log
2>&1 && \  
make | tee ${LOG_DIR}/${LOG_PKGCFG}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_PKGCFG}_make_install.log 2>&1 && \  
cd .. && rm -rf ${DIR_PKGCFG}  
# PCAP  
RUN wget -qO- ${URL_PCAP} | tar xz && \  
cd ${DIR_PCAP} && \  
./configure | tee ${LOG_DIR}/${LOG_PCAP}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_PCAP}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_PCAP}_make_install.log 2>&1 && \  
cd .. && rm -rf ${DIR_PCAP}  
# PCRE  
RUN wget -qO- ${URL_PCRE} | tar xz && \  
cd ${DIR_PCRE} && \  
./configure | tee ${LOG_DIR}/${LOG_PCRE}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_PCRE}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_PCRE}_make_install.log 2>&1 && \  
cd .. && rm -rf ${DIR_PCRE}  
# OpenSSL  
RUN wget -qO- ${URL_SSL} | tar xz && \  
cd ${DIR_SSL} && \  
./config  | tee ${LOG_DIR}/${LOG_SSL}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_SSL}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_SSL}_make_install.log 2>&1 && \  
cd .. && rm -rf ${DIR_SSL}  
# LuaJIT  
RUN echo ${URL_LUAJIT} && wget -qO- ${URL_LUAJIT} | tar xz && \  
cd ${DIR_LUAJIT} && \  
./configure | tee ${LOG_DIR}/${LOG_LUAJIT}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_LUAJIT}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_LUAJIT}_make_install.log 2>&1 && \  
cd .. && rm -rf ${DIR_LUAJIT}  
# hwloc  
RUN wget -qO- ${URL_HWLOC} | tar xz && \  
cd ${DIR_HWLOC} && \  
./configure | tee ${LOG_DIR}/${LOG_HWLOC}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_HWLOC}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_HWLOC}_make_install.log 2>&1 && \  
cd .. && rm -rf ${DIR_HWLOC}  
# lidnet  
RUN git clone ${URL_LIBDNET} && \  
cd ${DIR_LIBDNET} && \  
./configure | tee ${LOG_DIR}/${LOG_LIBDNET}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_LIBDNET}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_LIBDNET}_make_install.log 2>&1 && \  
cd .. && rm -rf ${DIR_LIBDNET}  
# SafeC  
RUN wget -qO- ${URL_SAFEC} | tar xz && \  
cd ${DIR_SAFEC} && \  
./configure | tee ${LOG_DIR}/${LOG_SAFEC}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_SAFEC}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_SAFEC}_make_install.log 2>&1 && \  
cd .. && rm -rf ${DIR_SAFEC}  
# Ragel  
RUN wget -qO- ${URL_RAGEL} | tar xz && \  
cd ${DIR_RAGEL} && \  
./configure | tee ${LOG_DIR}/${LOG_RAGEL}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_RAGEL}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_RAGEL}_make_install.log 2>&1 && \  
cd .. && rm -rf ${DIR_RAGEL}  
# Hyperscan  
RUN wget -qO- ${URL_BOOST} | tar xz && \  
wget -qO- ${URL_HYPERSCAN} | tar xz && \  
mkdir ${DIR_HYPERSCAN}-build && cd ${DIR_HYPERSCAN}-build && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr/local \  
-DBOOST_ROOT=${DOWNLOAD_DIR}/${DIR_BOOST}/ \  
../${DIR_HYPERSCAN} \  
| tee ${LOG_DIR}/${LOG_HYPERSCAN}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_HYPERSCAN}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_HYPERSCAN}_make_install.log 2>&1 && \  
./bin/unit-hyperscan && \  
cd .. && rm -rf ${DIR_HYPERSCAN} && rm -rf ${DIR_HYPERSCAN}-build && \  
rm -rf ${DIR_BOOST}  
# DAQ  
RUN wget -qO- ${URL_DAQ} | tar xz && \  
cd ${DIR_DAQ} && \  
./configure | tee ${LOG_DIR}/${LOG_DAQ}_configure.log 2>&1 && \  
make | tee ${LOG_DIR}/${LOG_DAQ}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_DAQ}_make_install.log 2>&1 && \  
ldconfig && \  
cd .. && rm -rf ${DIR_DAQ}  
# Snort  
RUN git clone ${URL_SNORT_GIT} && \  
cd ${DIR_SNORT_GIT} && \  
git checkout tags/${TAG_SNORT} && \  
./configure_cmake.sh \--prefix=${SNORT_INSTALL} \  
| tee ${LOG_DIR}/${LOG_SNORT}_configure.log 2>&1 && \  
cd build && \  
make -j 8 | tee ${LOG_DIR}/${LOG_SNORT}_make.log 2>&1 && \  
make install | tee ${LOG_DIR}/${LOG_SNORT}_make_install.log 2>&1 && \  
ln -s ${SNORT_INSTALL}/bin/snort /usr/sbin/snort && \  
cd .. && rm -rf ${DIR_SNORT_GIT}  
# Eclipse  
RUN wget -qO- ${URL_ECLIPSE} | tar xz && \  
mv ${DIR_ECLIPSE} /opt/  
  
# Create Eclipse Project (cmake) from
Source-------------------------------------------------------------------------------/  
# Uncomment to setup workspace and generate Eclipse CDT project with cmake,
for initial setup.  
#  
# Note: remove -v "$(cmd)/<snort-project>:${SNORT_PROJECT}"  
# -v "$(cmd)/<workspace>:${ECLIPSE_WORKSPACE}"  
#  
# from `eclipse.run` to prevent the script from overriding the created files.  
#  
# * You can copy the project and workspace, after including it via Eclipse IDE
and  
# comment out the section below again.  
#  
# * Copy the two folders workspace/ and snort-project/ and add them via -v
switch  
# to the container in the `eclipse.run` startup script (example, see above).  
#
-------------------------------------------------------------------------------------------------------------------------/  
RUN echo ${SNORT_PROJECT} && \  
echo ${ECLIPSE_WORKSPACE} && \  
mkdir -p ${SNORT_PROJECT} && \  
mkdir -p ${ECLIPSE_WORKSPACE} && \  
cd ${SNORT_PROJECT}/.. && \  
git clone ${URL_SNORT_GIT} && \  
cd ${SNORT_PROJECT} && \  
cmake -G"Eclipse CDT4 - Unix Makefiles" \  
-D_ECLIPSE_VERSION=4.7 \  
-DCMAKE_BUILD_TYPE=Debug \  
-DCMAKE_ECLIPSE_GENERATE_SOURCE_PROJECT=TRUE \  
-DCMAKE_ECLIPSE_MAKE_ARGUMENTS=-j4 \  
../${DIR_SNORT_GIT}  
# Set permissions  
RUN chmod 777 /home/${USERNAME} && \  
chown -R ${USERNAME}:${USERNAME} /home/${USERNAME} && \  
chmod 777 ${DOWNLOAD_DIR} && \  
chmod 777 ${LOG_DIR}  
  
USER ${USERNAME}  
CMD ["/bin/bash"]  


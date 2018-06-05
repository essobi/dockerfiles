FROM centos:centos6  
  
MAINTAINER David Muriel <dmuriel@bitergia.com>, Alberto Martín
<alberto.martin@bitergia.com>  
  
ENV ORION_USER orion  
ENV GIT_REV_ORION_PROXYCOAP 749e22376664dd3adae17492090e58882d3b28a7  
ENV GIT_REV_ORION 0.23.0  
  
RUN adduser --comment "${ORION_USER}" ${ORION_USER}  
  
WORKDIR /opt  
  
# Install EPEL repository (needed for some packages)  
RUN yum -y install epel-release && \  
# Install building tools  
yum -y install tar which nc bzip2 git make cmake gcc-c++ scons clang && \  
# Install dependencies  
yum -y install libmicrohttpd-devel boost-devel libcurl-devel CUnit-devel && \  
# Install mongodb driver from source  
curl -kOL https://github.com/mongodb/mongo-cxx-
driver/archive/legacy-1.0.2.tar.gz && \  
tar xfz legacy-1.0.2.tar.gz && \  
cd mongo-cxx-driver-legacy-1.0.2 && \  
scons install --prefix=/usr/local && \  
cd /opt && \  
# Install rapidjson from source  
curl -kOL https://github.com/miloyip/rapidjson/archive/v1.0.2.tar.gz && \  
tar xfz v1.0.2.tar.gz && \  
mv rapidjson-1.0.2/include/rapidjson/ /usr/local/include && \  
# Install Google Test/Mock from source  
curl -kOL http://googlemock.googlecode.com/files/gmock-1.5.0.tar.bz2 && \  
tar xfj gmock-1.5.0.tar.bz2 && \  
cd gmock-1.5.0 && \  
./configure && \  
make && \  
make install && \  
ldconfig && \  
cd /opt && \  
# Install proxyCoap  
git clone https://github.com/staropram/cantcoap && \  
cd cantcoap && \  
git checkout ${GIT_REV_ORION_PROXYCOAP} && \  
make && \  
cp cantcoap.h dbg.h nethelper.h /usr/local/include && \  
cp libcantcoap.a /usr/local/lib && \  
cd /opt && \  
# Install orion from source  
git clone https://github.com/telefonicaid/fiware-orion && \  
cd fiware-orion && \  
git checkout ${GIT_REV_ORION} && \  
make && \  
make install && \  
# reduce size of installed binaries  
strip /usr/bin/contextBroker && \  
strip /usr/bin/proxyCoap && \  
# create needed log and run paths  
mkdir -p /var/log/contextBroker && \  
mkdir -p /var/run/contextBroker && \  
chown ${ORION_USER} /var/log/contextBroker && \  
chown ${ORION_USER} /var/run/contextBroker && \  
cd /opt && \  
# cleanup sources, dev tools and yum cache to reduce the final image size  
rm -rf /opt/legacy-1.0.2.tar.gz \  
/opt/mongo-cxx-driver-legacy-1.0.2 \  
/usr/local/include/mongo \  
/usr/local/lib/libmongoclient.a \  
/opt/rapidjson-1.0.2 \  
/opt/v1.0.2.tar.gz \  
/usr/local/include/rapidjson \  
/opt/gmock-1.5.0.tar.bz2 \  
/opt/gmock-1.5.0 \  
/usr/local/bin/gmock* \  
/usr/local/bin/gtest* \  
/usr/local/include/gmock \  
/usr/local/include/gtest \  
/usr/local/lib/libgmock* \  
/usr/local/lib/libgtest* \  
/usr/local/share/aclocal/gtest* \  
/opt/cantcoap \  
/usr/local/include/cantcoap.h \  
/usr/local/include/dbg.h \  
/usr/local/include/nethelper.h \  
/usr/local/lib/libcantcoap.a \  
/opt/fiware-orion \  
&& \  
yum -y erase git perl rsync \  
cmake libarchive \  
gcc-c++ cloog-ppl cpp gcc glibc-devel glibc-headers \  
kernel-headers libgomp libstdc++-devel mpfr ppl \  
scons libmicrohttpd-devel boost-devel libcurl-devel \  
clang llvm llvm-libs \  
CUnit-devel CUnit \  
autoconf automake m4 libidn-devel \  
boost-wave boost-serialization boost-python \  
boost-iostreams boost boost-date-time \  
boost-test boost-graph boost-signals \  
boost-program-options boost-math \  
openssh openssh-clients libedit \  
&& \  
yum clean all  
  
WORKDIR /  
  
COPY docker-entrypoint.sh /  
ADD https://raw.githubusercontent.com/Bitergia/docker/master/utils/entrypoint-
common.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/bin/contextBroker"]  
  
### Exposed ports  
# - Default Orion port  
EXPOSE 1026  


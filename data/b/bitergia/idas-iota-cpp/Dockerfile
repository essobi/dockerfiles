FROM centos:6  
MAINTAINER Bitergia <fiware-testing@bitergia.com>  
  
ENV GIT_URL_IOTACPP https://github.com/telefonicaid/fiware-IoTAgent-
Cplusplus.git  
ENV GIT_REV_IOTACPP 1.2.1  
ENV GIT_PATH_IOTACPP /opt/iotacpp  
ENV IOTACPP_BUILD_TYPE Release  
ENV IOTACPP_USER iotagent  
  
# Install dependencies  
RUN yum -y install tar gzip unzip file nc which \  
cpp gcc gcc-c++ \  
automake autoconf libtool \  
git scons cmake \  
openssl-devel bzip2-devel zlib-devel \  
rpm-build && \  
git clone ${GIT_URL_IOTACPP} ${GIT_PATH_IOTACPP} && \  
cd ${GIT_PATH_IOTACPP} && \  
git checkout ${GIT_REV_IOTACPP} && \  
# Disable tests before compiling and fix mongo-cxx-driver git url  
sed -i CMakeLists.txt \  
-e 's|^add_test|#add_test|g' \  
-e 's|^add_subdirectory(tests)|#add_subdirectory(tests)|g' \  
-e 's|^enable_testing|#enable_testing|g' \  
-e 's|git@github.com:mongodb/mongo-cxx-driver.git|https://github.com/mongodb/mongo-cxx-driver|g' && \  
source tools/get_version_string.sh && \  
mkdir -p build/${IOTACPP_BUILD_TYPE} && \  
cd build/${IOTACPP_BUILD_TYPE} && \  
cmake -DGIT_VERSION=`get_rpm_version_string | cut -d ' ' -f 1` \  
-DGIT_COMMIT=`get_rpm_version_string | cut -d ' ' -f 2` \  
-DMQTT=ON \  
-DCMAKE_BUILD_TYPE=${IOTACPP_BUILD_TYPE} ../../ && \  
make install && \  
make package && \  
cd pack/Linux/RPM && \  
# Add mosquitto repository  
curl -kOL
http://download.opensuse.org/repositories/home:/oojah:/mqtt/CentOS_CentOS-6/home:oojah:mqtt.repo
&& \  
mv home:oojah:mqtt.repo /etc/yum.repos.d/ && \  
yum localinstall -y iot-agent-*.rpm && \  
cd /root && \  
# Enable services  
chkconfig iotagent on && \  
chkconfig mosquitto on && \  
# Cleanup to thin final image  
rm -rf ${GIT_PATH_IOTACPP} && \  
rm -rf /root/rpmbuild && \  
yum -y erase autoconf automake bzip2-devel \  
cmake cpp file gcc gcc-c++ git \  
libtool openssl-devel rpm-build \  
scons zlib-devel bzip2 cloog-ppl \  
elfutils elfutils-libs gdb glibc-devel \  
glibc-headers kernel-headers \  
keyutils-libs-devel krb5-devel \  
libarchive libcom_err-devel libgomp \  
libselinux-devel libsepol-devel \  
libstdc++-devel m4 mpfr patch perl \  
perl-Error perl-Git perl-Module-Pluggable \  
perl-Pod-Escapes perl-Pod-Simple \  
perl-libs perl-version \  
ppl rsync xz-lzma-compa && \  
yum clean all && \  
bash -c 'find /usr/share/locale -maxdepth 1 -mindepth 1 -type d | grep -v -e
"en_US" | xargs rm -rfv' && \  
bash -c 'localedef --list-archive | grep -v -e "en_US" | xargs localedef
--delete-from-archive' && \  
mv /usr/lib/locale/locale-archive /usr/lib/locale/locale-archive.tmpl && \  
build-locale-archive  
  
COPY config.json /etc/iot/  
RUN chown ${IOTACPP_USER}:${IOTACPP_USER} /etc/iot/config.json  
  
COPY docker-entrypoint.sh /  
ADD https://raw.githubusercontent.com/Bitergia/docker/master/utils/entrypoint-
common.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
### Exposed ports  
# - IoT Agent Admin port  
EXPOSE 8081  
# - IoT Agent port  
EXPOSE 8080  
# - Mosquitto  
EXPOSE 1883  


FROM centos  
MAINTAINER Maciej Czarnecki <mcczarny@gmail.com>  
ENV PATH="${PATH}:/opt/qt/5.9.1/gcc_64/bin/"  
ENV CMAKE_PREFIX_PATH="/opt/qt5.9.1/5.9.1/gcc_64/lib/cmake"  
ADD qt-installer-noninteractive.qs .  
RUN yum install -y epel-release centos-release-scl \  
&& yum install -y devtoolset-7-gcc maven devtoolset-7-gcc-c++ git rpm-build
rpmdevtools libstdc++-devel make boost boost-devel libcurl libcurl-devel
systemd-devel libuuid-devel java-1.8.0-openjdk-devel mesa-libGL-devel lcov \  
&& scl enable devtoolset-7 bash \  
&& curl -sSL https://download.qt.io/official_releases/online_installers/qt-
unified-linux-x64-online.run -o qt.run \  
&& chmod +x qt.run \  
&& curl -sSL https://cmake.org/files/v3.11/cmake-3.11.0-Linux-x86_64.sh -o
cmake.sh \  
&& chmod +x cmake.sh \  
&& sync \  
&& ./qt.run --platform minimal --script qt-installer-noninteractive.qs -v
--proxy \  
&& mkdir /opt/cmake3 \  
&& ./cmake.sh --prefix=/opt/cmake3/ \--exclude-subdir --skip-license \  
&& ln -s /opt/cmake3/bin/cmake /usr/bin/cmake3 \  
&& rm -rf \  
qt.run \  
cmake.sh \  
/var/lib/apt/lists/* \  
/opt/qt/update.rcc \  
/opt/qt/components.xml \  
/opt/qt/InstallationLog.txt \  
/opt/qt/MaintenanceTool* \  
/opt/qt/Tools \  
/opt/qt/Docs \  
/opt/qt/network.xml \  
/opt/qt/Examples \  
  
ENTRYPOINT [ "scl" "enable" "devtoolset-7" "--" ]  


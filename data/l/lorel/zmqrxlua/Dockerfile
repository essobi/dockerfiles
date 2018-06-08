FROM ubuntu:14.04.1  
  
ENV BUILD_PACKAGES cmake dh-autoreconf git gcc g++ libboost-chrono1.54-dev
libboost-system1.54-dev libcrypto++-dev libprotobuf-dev libprotobuf-c0-dev
make ocaml-nox protobuf-compiler protobuf-c-compiler python wget  
ENV UTIL_PACKAGES strace  
ENV DEPENDENCIES_PACKAGES libboost-chrono1.54.0 libboost-system1.54.0
libcrypto++9 libcurl4-openssl-dev liblua5.3-dev libprotobuf8 libprotobuf-c0  
  
ENV LINUX_SGX_GIT https://github.com/01org/linux-sgx.git  
ENV LINUX_SGX_COMMIT f4005be591a82b1bedfbf8021cec8929a3911bb1  
  
ENV LUA53_REPO deb http://ppa.launchpad.net/ubuntu-cloud-archive/mitaka-
staging/ubuntu trusty main  
  
ENV LUASGX_REPO git@github.com:Lorel/luasgx.git  
  
ENV SGX_BUILD_DIR /root/sgx-build  
ENV SGX_SDK_PARENT_DIR /opt/intel  
ENV SGX_SDK_DIR $SGX_SDK_PARENT_DIR/sgxsdk  
ENV LUA_BUILD_DIR /root/lua-build  
ENV LUASGX_BUILD_DIR /root/luasgx  
ENV RUNTIME_DIR /root/app  
  
ENV LUASGX_REPO_KEY /root/.ssh/id_rsa  
  
ADD build_files/.ssh/id_luasgx $LUASGX_REPO_KEY  
ADD build_files/docker_patches $SGX_BUILD_DIR  
  
# TODO: \--allow-unauthenticated added because libxml2 liblua5.3-0
liblua5.3-dev cannot be authenticated  
# should be fetched from http://ppa.launchpad.net/ubuntu-cloud-archive/mitaka-
staging/ubuntu  
# find a way to authenticate them  
  
RUN echo $LUA53_REPO >> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y --allow-unauthenticated $BUILD_PACKAGES $UTIL_PACKAGES
$DEPENDENCIES_PACKAGES && \  
mkdir -p $SGX_BUILD_DIR && \  
cd $SGX_BUILD_DIR && \  
git init && \  
git remote add origin $LINUX_SGX_GIT && \  
git fetch origin && \  
git checkout $LINUX_SGX_COMMIT && \  
git reset --hard && \  
patch linux/installer/bin/install-sgx-psw.bin.tmpl < 0001-Remove-modprobe-
lsmod-for-use-in-docker-container.patch && \  
patch linux/installer/common/psw/install.sh < 0002-Remove-unnecessary-sudo-
from-PSW-install-script.patch && \  
patch psw/ae/aesm_service/source/aesm/application/main.cpp < 0003-Remove-
daemonization-of-AESM.patch && \  
patch linux/installer/bin/install-sgx-sdk.bin.tmpl <
0004-use_INSTALL_PATH_var_for-ssdk_install.patch && \  
./download_prebuilt.sh && \  
make && \  
cd linux/installer/bin && \  
./build-installpkg.sh psw && \  
./sgx_linux_x64_psw_1.6.100.34922.bin && \  
./build-installpkg.sh sdk && \  
INSTALL_PATH=$SGX_SDK_PARENT_DIR ./sgx_linux_x64_sdk_1.6.100.34922.bin && \  
rm -rfv $SGX_BUILD_DIR && \  
cd /root && \  
wget
http://launchpadlibrarian.net/291946892/gcc-5-base_5.4.0-6ubuntu1~16.04.4_amd64.deb
&& \  
dpkg -i gcc-5-base_5.4.0-6ubuntu1~16.04.4_amd64.deb && \  
wget
http://launchpadlibrarian.net/291947015/libstdc++6_5.4.0-6ubuntu1~16.04.4_amd64.deb
&& \  
dpkg -i libstdc++6_5.4.0-6ubuntu1~16.04.4_amd64.deb && \  
wget http://launchpadlibrarian.net/236775583/libsodium18_1.0.8-5_amd64.deb &&
\  
dpkg -i libsodium18_1.0.8-5_amd64.deb && \  
wget http://launchpadlibrarian.net/247768967/libzmq5_4.1.4-6_amd64.deb && \  
dpkg -i libzmq5_4.1.4-6_amd64.deb && \  
wget http://launchpadlibrarian.net/247768966/libzmq5-dev_4.1.4-6_amd64.deb &&
\  
dpkg -i libzmq5-dev_4.1.4-6_amd64.deb && \  
rm gcc-5-base_5.4.0-6ubuntu1~16.04.4_amd64.deb
libstdc++6_5.4.0-6ubuntu1~16.04.4_amd64.deb libsodium18_1.0.8-5_amd64.deb
libzmq5_4.1.4-6_amd64.deb libzmq5-dev_4.1.4-6_amd64.deb && \  
mkdir -p $LUA_BUILD_DIR && \  
cd $LUA_BUILD_DIR && \  
git clone https://github.com/Lorel/lzmq.git && \  
cd lzmq && \  
mkdir cmake-make && \  
cd cmake-make && \  
cmake .. && \  
make install && \  
mkdir -p /usr/local/lib/lua/5.3/ && \  
mv /usr/local/lib/lua/lzmq /usr/local/lib/lua/5.3/lzmq && \  
mv /usr/local/lib/lua/lzmq.so /usr/local/lib/lua/5.3/lzmq.so && \  
rm -rf $LUA_BUILD_DIR/lzmq/ && \  
cd $LUA_BUILD_DIR && \  
git clone https://github.com/cloudwu/lua-cjson.git && \  
cd lua-cjson && \  
make install LUA_INCLUDE_DIR=/usr/include/lua5.3 LUA_VERSION=5.3 && \  
rm -rf $LUA_BUILD_DIR/lua-cjson && \  
cd $LUA_BUILD_DIR && \  
git clone https://github.com/Lorel/luacsv.git && \  
gcc -fPIC -I/usr/include/lua5.3/ -shared -O3 $LUA_BUILD_DIR/luacsv/csv.c -o
/usr/local/lib/lua/5.3/csv.so && \  
rm -rf $LUA_BUILD_DIR/luacsv/ && \  
wget -O /usr/local/lib/lua/5.3/rx.lua
https://raw.githubusercontent.com/bjornbytes/RxLua/master/rx.lua && \  
wget -O /usr/local/lib/lua/5.3/log.lua
https://raw.githubusercontent.com/Lorel/log.lua/master/log.lua && \  
cd $LUA_BUILD_DIR && \  
git clone https://github.com/Lorel/luadec && \  
cd luadec && \  
git submodule update --init lua-5.3 && \  
cd lua-5.3 && \  
make linux && \  
cd ../luadec && \  
make LUAVER=5.3 && \  
mv luadec /usr/bin && \  
rm -rfv $LUA_BUILD_DIR/luadec && \  
rmdir $LUA_BUILD_DIR && \  
chmod 400 $LUASGX_REPO_KEY && \  
ssh-keyscan -H github.com >> /root/.ssh/known_hosts && \  
cd /root && \  
mkdir -p $LUASGX_BUILD_DIR && \  
git clone $LUASGX_REPO $LUASGX_BUILD_DIR && \  
cd $LUASGX_BUILD_DIR/lua-sgx && \  
make && \  
cd $LUASGX_BUILD_DIR/app && \  
make && \  
mkdir -p $RUNTIME_DIR && \  
mv $LUASGX_BUILD_DIR/app/luasgx $RUNTIME_DIR/luasgx && \  
mv $LUASGX_BUILD_DIR/app/EnclavedLua.signed.so
$RUNTIME_DIR/EnclavedLua.signed.so && \  
rm -rfv $LUASGX_REPO_KEY $LUASGX_BUILD_DIR && \  
apt-get -y remove --auto-remove $BUILD_PACKAGES && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# add fancy Lua libs  
ADD build_files/zmq-rx.lua /usr/local/lib/lua/5.3/  
ADD build_files/sgx.lua /usr/local/lib/lua/5.3/  
ADD build_files/sgx-rx.lua /usr/local/lib/lua/5.3/  
  
ADD build_files/start.sh $RUNTIME_DIR  
  
WORKDIR $RUNTIME_DIR  
  
VOLUME ["/root/worker"]  
  
ENTRYPOINT ["./start.sh"]  


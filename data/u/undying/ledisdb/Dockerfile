  
FROM debian:8  
ENV color_on='\e[' color_off='\e[0m' color_red='31;1m' color_green='32;1m'
color_blue='34;1m'  
ENV TERM=screen TZ=UTC LC_ALL=C  
  
ENV leveldb_lib=/usr/local/lib/leveldb
leveldb_include=/usr/local/include/leveldb  
ENV rocksdb_lib=/usr/local/lib/rocksdb
rocksdb_include=/usr/local/include/rocksdb  
  
ENV ledisdb_v=0.6 leveldb_v=1.20 rocksdb_v=5.8.6  
ENV golang_v=1.9.2 GOROOT=/opt/go GOPATH=/go  
  
ENV build_deps="git wget build-essential" runtime_deps="ca-certificates"  
ENV ledisdb_build_deps="libsnappy-dev libgflags-dev"
ledisdb_runtime_deps="libsnappy1"  
COPY patches /tmp/patches  
  
RUN set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& export DEBIAN_CODENAME=$(sed -ne 's,VERSION=.*(\\([a-z]\\+\\))",\1,p'
/etc/os-release) \  
\  
&& sed -i 's|deb.debian.org|mirror.yandex.ru|' /etc/apt/sources.list \  
&& sed -i 's|security.debian.org|mirror.yandex.ru/debian-security|'
/etc/apt/sources.list \  
\  
&& printf "deb http://deb.debian.org/debian experimental main contrib non-
free\n" >> /etc/apt/sources.list \  
&& printf "deb http://deb.debian.org/debian jessie-backports main\n" >>
/etc/apt/sources.list.d/backports.list \  
\  
&& apt-get update -q \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
\--no-install-suggests \  
\--no-install-recommends \  
${build_deps} \  
${runtime_deps} \  
${ledisdb_build_deps} \  
${ledisdb_runtime_deps} \  
&& mkdir -p ${GOPATH}/src \  
\  
\  
&& bash -c 'printf "${color_on}${color_green}Downloading
Packages${color_off}\n"' \  
&& export CPU_COUNT=$(grep -c processor /proc/cpuinfo) \  
&& cd /opt && printf "\  
https://redirector.gvt1.com/edgedl/go/go${golang_v}.linux-amd64.tar.gz\n \  
https://github.com/siddontang/ledisdb/archive/v${ledisdb_v}.tar.gz\n \  
https://github.com/google/leveldb/archive/v${leveldb_v}.tar.gz\n \  
https://github.com/facebook/rocksdb/archive/v${rocksdb_v}.tar.gz\n \  
"|xargs -L1 -P${CPU_COUNT} -I{} wget -q {} \  
\  
&& ls *gz|xargs -P${CPU_COUNT} -L1 -I{} tar -xzpf {} && rm -v *gz \  
\  
\  
&& bash -c 'printf "${color_on}${color_green}Building LevelDB${color_off}\n"'
\  
\  
&& export ledisdb_gopath=/tmp/go/src/github.com/siddontang \  
&& mkdir -p ${ledisdb_gopath} && ln -s /opt/ledisdb-${ledisdb_v}
${ledisdb_gopath}/ledisdb \  
\  
&& cd /opt/leveldb-${leveldb_v} \  
&& patch -p0 < /opt/ledisdb-${ledisdb_v}/tools/leveldb.patch \  
&& make -j$(nproc) \  
\  
&& install -d ${leveldb_lib} \  
&& install out-shared/*.so* ${leveldb_lib} \  
&& install out-static/*.a* ${leveldb_lib} \  
&& cp -r include /usr/local/ \  
\  
\  
&& bash -c 'printf "${color_on}${color_green}Building RocksDB${color_off}\n"'
\  
&& cd /opt/rocksdb-${rocksdb_v} \  
&& make static_lib -j$(nproc) \  
&& install -d ${rocksdb_lib} \  
&& install librocksdb.a ${rocksdb_lib} \  
&& cp -r include /usr/local/ \  
\  
\  
&& bash -c 'printf "${color_on}${color_green}Building LedisDB${color_off}\n"'
\  
\  
&& mkdir -p ${GOPATH}/src/github.com/siddontang \  
&& ln -s /opt/ledisdb-${ledisdb_v} ${GOPATH}/src/github.com/siddontang/ledisdb
\  
\  
&& export CGO_CFLAGS="\  
-I${leveldb_include} \  
-I${rocksdb_include}" \  
&& export CGO_CXXFLAGS="${CGO_CFLAGS}" \  
&& export CGO_LDFLAGS="\  
-Wl,-rpath,${leveldb_lib} \  
-Wl,-rpath,${rocksdb_lib} \  
-L/usr/local/lib \  
-L${leveldb_lib} \  
-L${rocksdb_lib} \  
-lsnappy" \  
\  
&& export PATH=${PATH}:/opt/go/bin && export GOGC=off \  
&& export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${leveldb_lib}:${rocksdb_lib} \  
&& export DYLD_LIBRARY_PATH=${DYLD_LIBRARY_PATH}:${leveldb_lib}:${rocksdb_lib}
\  
\  
&& \  
for i in \  
github.com/peterh/liner \  
github.com/siddontang/goredis \  
;do \  
go get ${i} \  
;done \  
\  
&& cd /opt/ledisdb-${ledisdb_v} \  
&& find /tmp/patches/ledisdb -type f \  
|xargs -L1 -P$(nproc) -I{} bash -c 'patch --ignore-whitespace -p1 < {}' \  
\  
&& \  
for i in ledis-server ledis-cli ledis-benchmark ledis-dump ledis-load ledis-
repair;do \  
go build -i \  
-o /usr/local/bin/${i} \  
-tags 'snappy leveldb rocksdb' \  
cmd/${i}/* \  
;done \  
\  
\  
&& apt-get autoremove -y \  
${build_deps} \  
${ledisdb_build_deps} \  
&& apt-get clean \  
&& rm -rf \  
${GOROOT} \  
${GOPATH} \  
/var/lib/apt/lists/* /var/tmp/* /tmp/* /opt/*  
  
CMD [ "/usr/local/bin/ledis-server" ]  
  


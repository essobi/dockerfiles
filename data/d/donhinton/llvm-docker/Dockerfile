# start from base  
FROM gcc:6  
  
RUN set -ex; \  
apt-get -yqq update; \  
apt-get -yqq install \  
libedit-dev \  
libncurses5-dev \  
ninja-build \  
python2.7-dev \  
swig; \  
apt-get -yqq clean; \  
rm -rf /var/lib/apt/lists/*;  
  
RUN set -ex; \  
if ! command -v gpg > /dev/null; then \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
gnupg2 \  
dirmngr \  
; \  
rm -rf /var/lib/apt/lists/*; \  
fi  
  
ENV GPG_KEYS \  
# 4096R/345AD05D 2015-01-20 Hans Wennborg <hans@chromium.org>  
B6C8F98282B944E3B0D5C2530FC3042E345AD05D \  
# 2048R/02119294 2014-05-06 Tom Stellard <tstellar@redhat.com>  
11E521D646982372EB577A1F8F0871F202119294 \  
# 2048R/BB5A0569 2013-12-24 Bill Wendling <void@llvm.org>  
54E3BDE33185D9F69664D22455F5CD70BB5A0569 \  
# 4096R/7BFB4EDA 2014-06-16 Brad King <brad.king@kitware.com>  
CBA23971357C2E6590D9EFD3EC8FEF3A7BFB4EDA  
  
RUN set -ex; \  
for key in $GPG_KEYS; do \  
gpg --keyserver pgp.key-server.io --recv-keys "$key"; \  
done  
  
RUN set -ex; \  
curl -fSL https://cmake.org/files/v3.7/cmake-3.7.2-SHA-256.txt -o
cmake-3.7.2-SHA-256.txt; \  
curl -fSL https://cmake.org/files/v3.7/cmake-3.7.2-SHA-256.txt.asc -o
cmake-3.7.2-SHA-256.txt.asc; \  
curl -fSL https://cmake.org/files/v3.7/cmake-3.7.2-Linux-x86_64.tar.gz -o
cmake-3.7.2-Linux-x86_64.tar.gz; \  
gpg --verify cmake-3.7.2-SHA-256.txt.asc; \  
grep cmake-3.7.2-Linux-x86_64.tar.gz cmake-3.7.2-SHA-256.txt | sha256sum
--check; \  
tar -xf cmake-3.7.2-Linux-x86_64.tar.gz -C /usr/local --strip-components=1  
  
RUN set -ex; \  
curl -fSL https://releases.llvm.org/4.0.1/llvm-4.0.1.src.tar.xz -o
llvm.src.tar.xz; \  
curl -fSL https://releases.llvm.org/4.0.1/llvm-4.0.1.src.tar.xz.sig -o
llvm.src.tar.xz.sig; \  
gpg --batch --verify llvm.src.tar.xz.sig llvm.src.tar.xz; \  
mkdir -p /usr/src/llvm; \  
tar -xf llvm.src.tar.xz -C /usr/src/llvm --strip-components=1; \  
rm llvm.src.tar.xz*; \  
\  
curl -fSL https://releases.llvm.org/4.0.1/cfe-4.0.1.src.tar.xz -o
cfe.src.tar.xz; \  
curl -fSL https://releases.llvm.org/4.0.1/cfe-4.0.1.src.tar.xz.sig -o
cfe.src.tar.xz.sig; \  
gpg --batch --verify cfe.src.tar.xz.sig cfe.src.tar.xz; \  
mkdir -p /usr/src/llvm/tools/clang; \  
tar -xf cfe.src.tar.xz -C /usr/src/llvm/tools/clang --strip-components=1; \  
rm cfe.src.tar.xz*; \  
\  
curl -fSL https://releases.llvm.org/4.0.1/clang-tools-extra-4.0.1.src.tar.xz
-o clang-tools-extra.src.tar.xz; \  
curl -fSL https://releases.llvm.org/4.0.1/clang-tools-
extra-4.0.1.src.tar.xz.sig -o clang-tools-extra.src.tar.xz.sig; \  
gpg --batch --verify clang-tools-extra.src.tar.xz.sig clang-tools-
extra.src.tar.xz; \  
mkdir -p /usr/src/llvm/tools/clang/tools/extra; \  
tar -xf clang-tools-extra.src.tar.xz -C /usr/src/llvm/tools/clang/tools/extra
--strip-components=1; \  
rm clang-tools-extra.src.tar.xz*; \  
\  
curl -fSL https://releases.llvm.org/4.0.1/lldb-4.0.1.src.tar.xz -o
lldb.src.tar.xz; \  
curl -fSL https://releases.llvm.org/4.0.1/lldb-4.0.1.src.tar.xz.sig -o
lldb.src.tar.xz.sig; \  
gpg --batch --verify lldb.src.tar.xz.sig lldb.src.tar.xz; \  
mkdir -p /usr/src/llvm/tools/lldb; \  
tar -xf lldb.src.tar.xz -C /usr/src/llvm/tools/lldb --strip-components=1; \  
rm lldb.src.tar.xz*; \  
\  
curl -fSL https://releases.llvm.org/4.0.1/lld-4.0.1.src.tar.xz -o
lld.src.tar.xz; \  
curl -fSL https://releases.llvm.org/4.0.1/lld-4.0.1.src.tar.xz.sig -o
lld.src.tar.xz.sig; \  
gpg --batch --verify lld.src.tar.xz.sig lld.src.tar.xz; \  
mkdir -p /usr/src/llvm/tools/lld; \  
tar -xf lld.src.tar.xz -C /usr/src/llvm/tools/lld --strip-components=1; \  
rm lld.src.tar.xz*; \  
\  
curl -fSL https://releases.llvm.org/4.0.1/compiler-rt-4.0.1.src.tar.xz -o
compiler-rt.src.tar.xz; \  
curl -fSL https://releases.llvm.org/4.0.1/compiler-rt-4.0.1.src.tar.xz.sig -o
compiler-rt.src.tar.xz.sig; \  
gpg --batch --verify compiler-rt.src.tar.xz.sig compiler-rt.src.tar.xz; \  
mkdir -p /usr/src/llvm/projects/compiler-rt; \  
tar -xf compiler-rt.src.tar.xz -C /usr/src/llvm/projects/compiler-rt --strip-
components=1; \  
rm compiler-rt.src.tar.xz*; \  
\  
curl -fSL https://releases.llvm.org/4.0.1/libcxx-4.0.1.src.tar.xz -o
libcxx.src.tar.xz; \  
curl -fSL https://releases.llvm.org/4.0.1/libcxx-4.0.1.src.tar.xz.sig -o
libcxx.src.tar.xz.sig; \  
gpg --batch --verify libcxx.src.tar.xz.sig libcxx.src.tar.xz; \  
mkdir -p /usr/src/llvm/projects/libcxx; \  
tar -xf libcxx.src.tar.xz -C /usr/src/llvm/projects/libcxx --strip-
components=1; \  
rm libcxx.src.tar.xz*; \  
\  
curl -fSL https://releases.llvm.org/4.0.1/libcxxabi-4.0.1.src.tar.xz -o
libcxxabi.src.tar.xz; \  
curl -fSL https://releases.llvm.org/4.0.1/libcxxabi-4.0.1.src.tar.xz.sig -o
libcxxabi.src.tar.xz.sig; \  
gpg --batch --verify libcxxabi.src.tar.xz.sig libcxxabi.src.tar.xz; \  
mkdir -p /usr/src/llvm/projects/libcxxabi; \  
tar -xf libcxxabi.src.tar.xz -C /usr/src/llvm/projects/libcxxabi --strip-
components=1; \  
rm libcxxabi.src.tar.xz*; \  
\  
curl -fSL https://releases.llvm.org/4.0.1/libunwind-4.0.1.src.tar.xz -o
libunwind.src.tar.xz; \  
curl -fSL https://releases.llvm.org/4.0.1/libunwind-4.0.1.src.tar.xz.sig -o
libunwind.src.tar.xz.sig; \  
gpg --batch --verify libunwind.src.tar.xz.sig libunwind.src.tar.xz; \  
mkdir -p /usr/src/llvm/projects/libunwind; \  
tar -xf libunwind.src.tar.xz -C /usr/src/llvm/projects/libunwind --strip-
components=1; \  
rm libunwind.src.tar.xz*; \  
\  
curl -fSL https://releases.llvm.org/4.0.1/openmp-4.0.1.src.tar.xz -o
openmp.src.tar.xz; \  
curl -fSL https://releases.llvm.org/4.0.1/openmp-4.0.1.src.tar.xz.sig -o
openmp.src.tar.xz.sig; \  
gpg --batch --verify openmp.src.tar.xz.sig openmp.src.tar.xz; \  
mkdir -p /usr/src/llvm/projects/openmp; \  
tar -xf openmp.src.tar.xz -C /usr/src/llvm/projects/openmp --strip-
components=1; \  
rm openmp.src.tar.xz*;  
  
RUN set -ex; \  
mkdir /tmp/build && cd /tmp/build; \  
cmake \  
-GNinja \  
-DCMAKE_BUILD_TYPE=Release \  
-DLLVM_ENABLE_ASSERTIONS=ON \  
-DLLVM_PARALLEL_LINK_JOBS=1 \  
/usr/src/llvm 2>&1 | tee /var/log/llvm-build.log; \  
\  
ninja install 2>&1 | tee -a /var/log/llvm-build.log; \  
cd - && rm -rf /tmp/build;  


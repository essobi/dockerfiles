FROM centos:5  
ADD libc.conf /etc/ld.so.conf.d/libc.conf  
RUN yum upgrade -qy \  
&& yum install -qy epel-release  
RUN yum install -qy git vim-enhanced nano make gcc-c++ flex gdb wget
libidn.x86_64 patch gpg  
RUN gpg --keyserver keys.gnupg.net --recv-keys 7BFB4EDA  
RUN VERSION=3.6.1 \  
&& set -euxo pipefail \  
&& wget --no-verbose --no-check-certificate --directory-prefix /dev/shm
http://cmake.org/files/v${VERSION%.*}/cmake-${VERSION}-{SHA-256.txt{,.asc},Linux-x86_64.sh}
\  
&& gpg --verify /dev/shm/cmake-${VERSION}-SHA-256.txt{.asc,} \  
&& ( \  
cd /dev/shm \  
&& fgrep cmake-${VERSION}-Linux-x86_64.sh cmake-${VERSION}-SHA-256.txt |
sha256sum --check - \  
) \  
&& sh /dev/shm/cmake-${VERSION}-Linux-x86_64.sh --prefix=/usr/local --exclude-
subdir  
  
RUN yum install -qy \  
sudo \  
passwd \  
openssh-server \  
ed \  
readline-devel \  
zlib-devel \  
curl-devel \  
bzip2-devel \  
python-devel \  
apr-devel \  
libevent-devel \  
openssl-libs \  
openssl-devel \  
libyaml \  
libyaml-devel \  
epel-release \  
htop \  
perl-Env \  
perl-ExtUtils-Embed \  
libxml2-devel \  
libxslt-devel \  
libffi-devel \  
file \  
xz  
  
# https://gcc.gnu.org/mirrors.html  
RUN set -ex \  
&& for key in \  
B215C1633BCA0477615F1B35A5B3A004745C015A \  
B3C42148A44E6983B3E4CC0793FA9B1AB75C61B8 \  
90AA470469D3965A87A5DCB494D03953902C9419 \  
80F98B2E0DAB6C8281BDF541A7C8C3B2F71EDF1C \  
7F74F97C103468EE5D750B583AB00996FC26A641 \  
33C235A34C46AA3FFB293709A328C3A2C3C45C06; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
# Signing key for binutils and coreutils  
RUN gpg --keyserver keys.gnupg.net --recv-keys 4AE55E93 306037D9  
  
RUN set -exuo pipefail \  
&& VERSION=2.26 \  
&& curl -fS "http://ftp.gnu.org/gnu/binutils/binutils-${VERSION}.tar.gz" -o
binutils.tar.gz \  
&& curl -fS "http://ftp.gnu.org/gnu/binutils/binutils-${VERSION}.tar.gz.sig"
-o binutils.tar.gz.sig \  
&& gpg --batch --verify binutils.tar.gz.sig binutils.tar.gz \  
&& mkdir -p /usr/src/binutils \  
&& tar xf binutils.tar.gz -C /usr/src/binutils --strip-components=1 \  
&& BUILD="$(mktemp -d)" \  
&& pushd "${BUILD}" \  
&& /usr/src/binutils/configure \  
&& make -j16 \  
&& make install \  
&& rm -r /usr/src/binutils \  
&& popd \  
&& rm binutils.tar.gz{,.sig} \  
&& rm -r "${BUILD}"  
  
RUN set -exuo pipefail \  
&& VERSION=8.25 \  
&& curl -fS "http://ftp.gnu.org/gnu/coreutils/coreutils-${VERSION}.tar.xz" -o
coreutils.tar.xz \  
&& curl -fS "http://ftp.gnu.org/gnu/coreutils/coreutils-${VERSION}.tar.xz.sig"
-o coreutils.tar.xz.sig \  
&& gpg --batch --verify coreutils.tar.xz.sig coreutils.tar.xz \  
&& mkdir -p /usr/src/coreutils \  
&& xzcat coreutils.tar.xz | tar x -C /usr/src/coreutils --strip-components=1 \  
&& BUILD="$(mktemp -d)" \  
&& pushd "${BUILD}" \  
&& env FORCE_UNSAFE_CONFIGURE=1 /usr/src/coreutils/configure \  
&& make \  
&& make install \  
&& rm -r /usr/src/coreutils \  
&& popd \  
&& rm -r "${BUILD}"  
# "download_prerequisites" pulls down a bunch of tarballs and extracts them,  
# but then leaves the tarballs themselves lying around  
RUN GCC_VERSION=6.1.0 \  
&& set -exuo pipefail \  
&& curl -fSL
"http://ftpmirror.gnu.org/gcc/gcc-$GCC_VERSION/gcc-$GCC_VERSION.tar.bz2" -o
gcc.tar.bz2 \  
&& curl -fSL
"http://ftpmirror.gnu.org/gcc/gcc-$GCC_VERSION/gcc-$GCC_VERSION.tar.bz2.sig"
-o gcc.tar.bz2.sig \  
&& gpg --batch --verify gcc.tar.bz2.sig gcc.tar.bz2 \  
&& mkdir -p /usr/src/gcc \  
&& tar -xf gcc.tar.bz2 -C /usr/src/gcc --strip-components=1 \  
&& rm gcc.tar.bz2* \  
&& pushd /usr/src/gcc \  
&& ./contrib/download_prerequisites \  
&& { rm *.tar.* || true; } \  
&& popd \  
&& dir="$(mktemp -d)" \  
&& pushd "$dir" \  
&& /usr/src/gcc/configure \  
\--disable-multilib \  
\--enable-languages=c,c++ \  
&& make -j"$(nproc)" \  
&& make install-strip \  
&& popd \  
&& rm -r /usr/src/gcc \  
&& rm -rf "$dir"  
# gpg: key 18ADD4FF: public key "Benjamin Peterson <benjamin@python.org>"
imported  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF  
  
RUN set -ex \  
&& export PYTHON_VERSION=2.7.12 \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tgz"
-o python.tgz \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tgz.asc"
-o python.tgz.asc \  
&& gpg --batch --verify python.tgz.asc python.tgz \  
&& rm -r python.tgz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xC /usr/src/python --strip-components=1 -f python.tgz \  
&& rm python.tgz \  
\  
&& cd /usr/src/python \  
&& ./configure \  
\--enable-shared \  
\--enable-unicode=ucs4 \  
&& make -j"$(nproc)" \  
&& make install \  
&& ldconfig \  
&& curl -fSL 'https://bootstrap.pypa.io/get-pip.py' | python2 \  
&& pip install --no-cache-dir --upgrade pip \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python ~/.cache  


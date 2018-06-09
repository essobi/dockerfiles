FROM ubuntu:16.04  
  
# Install related packages and set LLVM 3.8 as the compiler  
RUN apt-get -q update && apt-get dist-upgrade -y && \  
apt-get -q install -y \  
build-essential \  
make \  
libc6-dev \  
clang-3.8 \  
curl \  
libedit-dev \  
python2.7 \  
python2.7-dev \  
libicu-dev \  
libssl-dev \  
libxml2 \  
libxml2-dev \  
tzdata \  
libcunit1-dev \  
libev-dev \  
libevent-dev \  
libjansson-dev \  
libjemalloc-dev \  
libc-ares-dev \  
libsystemd-dev \  
libspdylay-dev \  
zlib1g-dev \  
git \  
libcurl4-openssl-dev \  
pkg-config \  
libblocksruntime-dev \  
&& update-alternatives \--quiet --install /usr/bin/clang clang
/usr/bin/clang-3.8 100 \  
&& update-alternatives \--quiet --install /usr/bin/clang++ clang++
/usr/bin/clang++-3.8 100 \  
&& rm -r /var/lib/apt/lists/*  
  
# Download and Install nghttp2 & curl  
RUN curl -LOk
https://github.com/nghttp2/nghttp2/releases/download/v1.22.0/nghttp2-1.22.0.tar.bz2
\  
&& tar xf nghttp2-1.22.0.tar.bz2 && rm nghttp2-1.22.0.tar.bz2 && cd
nghttp2-1.22.0 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf nghttp2-1.22.0  
RUN curl -LOk
https://github.com/curl/curl/releases/download/curl-7_54_0/curl-7.54.0.tar.bz2
\  
&& tar xf curl-7.54.0.tar.bz2 && rm curl-7.54.0.tar.bz2 && cd curl-7.54.0 \  
&& ./configure --with-nghttp2=/usr/local --with-ssl \  
&& make \  
&& make install \  
&& ldconfig \  
&& cd .. \  
&& rm -rf curl-7.54.0  
  
# Everything up to here should cache nicely between Swift versions, assuming
dev dependencies change little  
ARG SWIFT_PLATFORM=ubuntu16.04  
ARG SWIFT_BRANCH=swift-4.0.3-release  
ARG SWIFT_VERSION=swift-4.0.3-RELEASE  
  
ENV SWIFT_PLATFORM=$SWIFT_PLATFORM \  
SWIFT_BRANCH=$SWIFT_BRANCH \  
SWIFT_VERSION=$SWIFT_VERSION  
  
# Download GPG keys, signature and Swift package, then unpack, cleanup and
execute permissions for foundation libs  
RUN SWIFT_URL=https://swift.org/builds/$SWIFT_BRANCH/$(echo "$SWIFT_PLATFORM"
| tr -d .)/$SWIFT_VERSION/$SWIFT_VERSION-$SWIFT_PLATFORM.tar.gz \  
&& curl -fSsL $SWIFT_URL -o swift.tar.gz \  
&& curl -fSsL $SWIFT_URL.sig -o swift.tar.gz.sig \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --quiet --keyserver ha.pool.sks-keyservers.net --recv-keys
"7463A81A4B2EEA1B551FFBCFD441C977412B37AD"
"5E4DF843FB065D7F7E24FBA2EF5430F071E1B235" \  
&& gpg --batch --verify --quiet swift.tar.gz.sig swift.tar.gz \  
&& tar -xzf swift.tar.gz --directory / --strip-components=1 \  
&& rm -r "$GNUPGHOME" swift.tar.gz.sig swift.tar.gz \  
&& chmod -R o+r /usr/lib/swift  
  
RUN apt-get -y remove --purge curl  
  
# Print Installed Swift Version  
RUN swift --version  


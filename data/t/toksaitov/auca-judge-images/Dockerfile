# Use the `auca-judge-agent:fat` image with Ubuntu as a base image.  
FROM toksaitov/auca-judge-agent:fat  
  
# Install Apple Swift.  
# Based on `docker-swift` maintained by Haris Amin at  
# https://github.com/swiftdocker/docker-
swift/blob/94a43272fe6411c12045414cfc797d3c0bcf2823/Dockerfile  
# licensed under the MIT License.  
#  
# ===  
# Install related packages and set LLVM 3.6 as the compiler  
RUN apt-get -q update && \  
apt-get -q install -y \  
make \  
libc6-dev \  
clang-3.6 \  
curl \  
libedit-dev \  
python2.7 \  
python2.7-dev \  
libicu-dev \  
rsync \  
libxml2 \  
git \  
libcurl4-openssl-dev \  
&& update-alternatives --quiet --install /usr/bin/clang clang
/usr/bin/clang-3.6 100 \  
&& update-alternatives --quiet --install /usr/bin/clang++ clang++
/usr/bin/clang++-3.6 100 \  
&& rm -r /var/lib/apt/lists/*  
  
# Everything up to here should cache nicely between Swift versions, assuming
dev dependencies change little  
ENV SWIFT_BRANCH=swift-3.0.2-release \  
SWIFT_VERSION=swift-3.0.2-RELEASE \  
SWIFT_PLATFORM=ubuntu16.04 \  
PATH=/usr/bin:$PATH  
  
# Download GPG keys, signature and Swift package, then unpack and cleanup  
RUN SWIFT_URL=https://swift.org/builds/$SWIFT_BRANCH/$(echo "$SWIFT_PLATFORM"
| tr -d .)/$SWIFT_VERSION/$SWIFT_VERSION-$SWIFT_PLATFORM.tar.gz \  
&& curl -fSsL $SWIFT_URL -o swift.tar.gz \  
&& curl -fSsL $SWIFT_URL.sig -o swift.tar.gz.sig \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& set -e; \  
for key in \  
# pub 4096R/412B37AD 2015-11-19 [expires: 2017-11-18]  
# Key fingerprint = 7463 A81A 4B2E EA1B 551F FBCF D441 C977 412B 37AD  
# uid Swift Automatic Signing Key #1 <swift-infrastructure@swift.org>  
7463A81A4B2EEA1B551FFBCFD441C977412B37AD \  
# pub 4096R/21A56D5F 2015-11-28 [expires: 2017-11-27]  
# Key fingerprint = 1BE1 E29A 084C B305 F397 D62A 9F59 7F4D 21A5 6D5F  
# uid Swift 2.2 Release Signing Key <swift-infrastructure@swift.org>  
1BE1E29A084CB305F397D62A9F597F4D21A56D5F \  
# pub 4096R/91D306C6 2016-05-31 [expires: 2018-05-31]  
# Key fingerprint = A3BA FD35 56A5 9079 C068 94BD 63BC 1CFE 91D3 06C6  
# uid Swift 3.x Release Signing Key <swift-infrastructure@swift.org>  
A3BAFD3556A59079C06894BD63BC1CFE91D306C6 \  
; do \  
gpg --quiet --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done \  
&& gpg --batch --verify --quiet swift.tar.gz.sig swift.tar.gz \  
&& tar -xzf swift.tar.gz --directory / --strip-components=1 \  
&& rm -r "$GNUPGHOME" swift.tar.gz.sig swift.tar.gz  
  
# ===  
# Create a working directory for the build agent (specified in the agent's  
# configuration file).  
RUN mkdir /submission  
  
# Expose the build agent's communication port (set in the agent's  
# configuration file).  
EXPOSE 7742  


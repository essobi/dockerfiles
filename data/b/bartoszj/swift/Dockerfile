FROM debian:jessie  
MAINTAINER Bartosz Janda  
  
ENV SWIFT_VERSION swift-3.1-RELEASE  
ENV SWIFT_BRANCH swift-3.1-release  
ENV SWIFT_PLATFORM jessie  
  
# Install dependencies  
RUN apt-get update && apt-get install --no-install-recommends -y \  
binutils \  
clang \  
libcurl4-openssl-dev \  
libedit2 \  
libicu-dev \  
make \  
  
libpython2.7 \  
libxml2 \  
  
ca-certificates \  
curl \  
dirmngr \  
git \  
gnupg \  
rsync \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download GPG keys, signature and Swift package, then unpack and cleanup  
RUN GNUPGHOME="$(mktemp -d)" \  
&& SWIFT_ARCHIVE="${SWIFT_VERSION}-${SWIFT_PLATFORM}.tar.gz" \  
&& SWIFT_ARCHIVE_SIGNATURE="${SWIFT_ARCHIVE}.asc" \  
  
&& curl -fSsL
"https://bintray.com/user/downloadSubjectPublicKey?username=bartoszj" | gpg
--import \- \  
&& curl -fSL#
"https://dl.bintray.com/bartoszj/Swift/${SWIFT_BRANCH}/${SWIFT_VERSION}/${SWIFT_ARCHIVE}"
-o "${SWIFT_ARCHIVE}" \  
&& curl -fSsL
"https://dl.bintray.com/bartoszj/Swift/${SWIFT_BRANCH}/${SWIFT_VERSION}/${SWIFT_ARCHIVE_SIGNATURE}"
-o "${SWIFT_ARCHIVE_SIGNATURE}" \  
&& gpg --verify "${SWIFT_ARCHIVE_SIGNATURE}" \  
&& tar -zxvf "${SWIFT_ARCHIVE}" \--directory / \  
  
&& rm -r "${GNUPGHOME}" "${SWIFT_ARCHIVE}" "${SWIFT_ARCHIVE_SIGNATURE}"  
  
CMD ["swift"]  


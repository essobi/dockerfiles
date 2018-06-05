# Multistage build for the image with splitsh-lite binary.  
# See https://docs.docker.com/engine/userguide/eng-image/multistage-build/  
# Requires Docker 17.05 or later.  
# The git2go library needs specific versions of golang  
# (keep checking what's working or broken at https://travis-
ci.org/libgit2/git2go):  
FROM golang:1.8.3-stretch as builder  
  
# We need cmake to run the git2go build script, and the SSL & SSH  
# libraries for a completely working libgit2; note that a final statically  
# linked binary would be nice, but the usual recipes for this don't work here.  
RUN apt-get update && \  
apt-get install -y \  
cmake \  
libssl-dev \  
libssh2-1-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& cd "$GOPATH" \  
&& go get github.com/boltdb/bolt \  
&& git clone https://github.com/libgit2/git2go.git
"${GOPATH}/src/github.com/libgit2/git2go" \  
&& cd "${GOPATH}/src/github.com/libgit2/git2go" \  
&& git checkout 7969aefd42abf3d3d93397760e54c872493e0972 \  
&& git submodule update --init \  
&& make test-static \  
&& go install --tags "static" ./... \  
&& git clone -b UADIGITAL-739 https://github.com/ltrr-arizona-edu/lite
"${GOPATH}/src/github.com/splitsh/lite" \  
&& cd "$GOPATH" \  
&& go build --tags "static" github.com/splitsh/lite \  
&& go install --tags "static" github.com/splitsh/lite  
  
# The image specified here should be compatible with the builder image (it  
# might not be the latest version, but should match the base used there).  
FROM debian:stretch  
  
# Copy in the executable binary from the previous phase.  
COPY \--from=builder "${GOPATH:-/go}/bin/lite" /usr/local/bin/  
  
WORKDIR /root/  
# Add the standard packaged version of Git and the scripts for splitting &c.  
RUN apt-get update && \  
apt-get install -y \  
git \  
curl \  
&& ln -fs /usr/share/zoneinfo/America/Phoenix /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& rm -r /var/lib/apt/lists/* \  
&& cd /tmp \  
&& git clone -b '1.4.1'
https://bitbucket.org/ua_drupal/uaqs_repository_tools.git \  
&& cp uaqs_repository_tools/splitmono.sh /usr/local/bin/splitmono \  
&& cp uaqs_repository_tools/tagsplits.sh /usr/local/bin/tagsplits \  
&& cp uaqs_repository_tools/addtomono.sh /usr/local/bin/addtomono \  
&& rm -Rf uaqs_repository_tools  


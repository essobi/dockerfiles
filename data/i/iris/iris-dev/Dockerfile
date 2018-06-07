# Copyright (c) 2014 Project Iris. All rights reserved.  
#  
# The current Docker container is part of the official image collection of the  
# Iris cloud messaging system, and as such, the same licensing terms apply.  
# For details please see http://iris.karalabe.com/downloads#License  
# Iris node container of the latest development branch.  
FROM iris/base  
  
MAINTAINER Péter Szilágyi <peterke@gmail.com>  
  
# Install the prerequisites to build Iris locally, download and build the
latest  
# Go release, fetch and compile Iris from sources, deploy and clean everything  
# up to reduce the container size.  
RUN \  
echo "Installing build prerequisites" && \  
apt-get update && \  
apt-get install -y git mercurial gcc && \  
\  
echo "Downloading and building the Go release" && \  
hg clone -u release https://code.google.com/p/go && \  
cd go/src && ./all.bash && \  
export GOROOT=/go && \  
export GOPATH=/go-tmp && \  
export PATH=$GOROOT/bin:$PATH && \  
\  
echo "Downloading and building Iris" && \  
go get github.com/project-iris/iris && \  
mv $GOPATH/bin/iris $IRIS_BIN && \  
\  
echo "Cleaning up build environment" && \  
rm -r -f /go /go-tmp && \  
apt-get autoremove -y git mercurial gcc  


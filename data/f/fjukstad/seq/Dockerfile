FROM ubuntu:16.10  
# Install Pachyderm and its dependencies  
RUN \  
apt-get update -yq && \  
apt-get install -yq --no-install-recommends \  
git \  
ca-certificates \  
curl \  
fuse && \  
apt-get clean && \  
rm -rf /var/lib/apt  
  
# Install Go 1.6.0 (if you don't already have it in your base image)  
RUN \  
curl -sSL https://storage.googleapis.com/golang/go1.6.linux-amd64.tar.gz | tar
-C /usr/local -xz && \  
mkdir -p /go/bin  
ENV PATH
/usr/local/go/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin  
ENV GOPATH /go  
ENV GOROOT /usr/local/go  
  
# Install Pachyderm job-shim  
RUN go get github.com/pachyderm/pachyderm && \  
go get github.com/pachyderm/pachyderm/src/server/cmd/job-shim && \  
cp $GOPATH/bin/job-shim /job-shim  
  
RUN apt-get update  
  
# Get other common pkgs for seq  
RUN apt-get install -y \  
build-essential \  
zlib1g-dev \  
libncurses5-dev \  
default-jre \  
wget \  
unzip  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
# Set up tool dir where everything should be installed  
RUN mkdir /tools  
WORKDIR /tools  
  
# Set up worker user  
RUN groupadd -g 1001 workergroup  
RUN useradd -g 1001 -u 1000 -p $(openssl passwd -1 worker) worker  
RUN mkdir /home/worker  
WORKDIR /home/worker  
RUN chown worker:workergroup /home/worker  
RUN chown -R worker:workergroup /tools  
  
# link up everything and add to path  
USER worker  


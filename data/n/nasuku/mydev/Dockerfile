FROM ubuntu:16.10  
MAINTAINER Suresh Nalluru <nasuku@yahoo.com>  
  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" | tee /etc/apt/sources.list.d/bazel.list  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
  
# alternative way to add rge key without install curl  
#ADD https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg /  
#RUN apt-key add /apt-key.pub.gpg && rm /apt-key.pub.gpg  
# running apt-get as a separate step anyway and keeping the /var so that in
the future I can install new pkgs.  
RUN apt-get update \  
&& apt-get install -y curl  
RUN curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | apt-
key add -  
RUN apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get -y --no-install-recommends install \  
dkms \  
g++ \  
gcc \  
gdb \  
git \  
iproute2 \  
make \  
net-tools \  
python \  
vim  
  
# the heavy weight components - add as separate layer  
RUN apt-get -y --no-install-recommends install oracle-java8-installer bazel  
  
# from https://github.com/docker-
library/golang/blob/85df9970e9548f38248d36f6f4341e2aea128515/1.7/Dockerfile  
ENV GOLANG_VERSION 1.7.1  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
43ad621c9b014cde8db17393dc108378d37bc853aa351a6c74bf6432c1bbd182  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
ADD https://raw.githubusercontent.com/docker-
library/golang/85df9970e9548f38248d36f6f4341e2aea128515/1.7/wheezy/go-wrapper
/usr/local/bin/go-wrapper  
  
#WORKDIR $GOPATH  
# apt-get -y install default-jre  
# apt-get build-dep --no-install-recommends --only-source linux  


FROM ubuntu:xenial  
  
# Based on
https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/docker  
# maintener info  
MAINTAINER Lukasz Pyrzyk <lukasz.pyrzyk@gmail.com>, Jakub Bentkowski
<bentkowski.jakub@gmail.com>  
  
# Update and install dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
pkg-config \  
software-properties-common \  
build-essential \  
curl \  
git \  
libcurl3-dev \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python-dev \  
rsync \  
unzip \  
zip \  
zlib1g-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -fSsL -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
  
RUN pip --no-cache-dir install \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
sklearn \  
&& \  
python -m ipykernel.kernelspec  
  
# Set up Bazel.  
# We need to add a custom PPA to pick up JDK8, since trusty doesn't  
# have an openjdk8 backport. openjdk-r is maintained by a reliable
contributor:  
# Matthias Klose (https://launchpad.net/~doko). It will do until  
# we either update the base image beyond 14.04 or openjdk-8 is  
# finally backported to trusty; see e.g.  
# https://bugs.launchpad.net/trusty-backports/+bug/1368094  
RUN add-apt-repository -y ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y --no-install-recommends openjdk-8-jdk openjdk-8-jre-
headless && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Running bazel inside a `docker build` command causes trouble, cf:  
# https://github.com/bazelbuild/bazel/issues/134  
# The easiest solution is to set up a bazelrc file forcing --batch.  
RUN echo "startup --batch" >>/root/.bazelrc  
# Similarly, we need to workaround sandboxing issues:  
# https://github.com/bazelbuild/bazel/issues/418  
RUN echo "build --spawn_strategy=standalone --genrule_strategy=standalone" \  
>>/root/.bazelrc  
ENV BAZELRC /root/.bazelrc  
  
# Install the most recent bazel release.  
ENV BAZEL_VERSION 0.3.2  
WORKDIR /  
RUN mkdir /bazel && \  
cd /bazel && \  
curl -fSsL -O
https://github.com/bazelbuild/bazel/releases/download/$BAZEL_VERSION/bazel-$BAZEL_VERSION-
installer-linux-x86_64.sh && \  
curl -fSsL -o /bazel/LICENSE.txt
https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE.txt && \  
chmod +x bazel-*.sh && \  
./bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \  
cd / && \  
rm -f /bazel/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh  
  
RUN echo $(g++ --version)  
RUN echo $(bazel version)  


FROM ubuntu:16.04  
  
LABEL maintainer="Adithya Seshadri <a.seshadri@samsung.com>"  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 BAZELRC=/root/.bazelrc BAZEL_VERSION=0.5.4  
  
RUN apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository ppa:ubuntu-toolchain-r/test -y && \  
apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates
\  
build-essential \  
curl \  
libcurl3-dev \  
git \  
libstdc++6 \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
pkg-config \  
python3-dev \  
python3-pip \  
python3-setuptools \  
unzip \  
software-properties-common \  
swig \  
zip \  
zlib1g-dev \  
libcurl3-dev \  
openjdk-8-jdk\  
openjdk-8-jre-headless \  
wget \  
vim \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
ln -s /usr/bin/python3 /usr/bin/python && \  
ln -s /usr/bin/pip3 /usr/bin/pip && \  
ln -s /usr/bin/easy_install3 /usr/bin/easy_install  
  
RUN pip --no-cache-dir install \  
mock \  
grpcio \  
virtualenv \  
tensorflow\  
sklearn \  
pandas \  
scipy \  
jupyter \  
notebook \  
tensorflow-serving-api-python3 \  
pyspark  
  
RUN mkdir /bazel && \  
cd /bazel && \  
curl -fSsL -O
https://github.com/bazelbuild/bazel/releases/download/$BAZEL_VERSION/bazel-$BAZEL_VERSION-
installer-linux-x86_64.sh && \  
curl -fSsL -o /bazel/LICENSE.txt
https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE && \  
chmod +x bazel-*.sh && \  
./bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \  
cd / && \  
rm -f /bazel/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \  
TEMP_DEB="$(mktemp)" && \  
wget -O "$TEMP_DEB" 'http://storage.googleapis.com/tensorflow-serving-
apt/pool/tensorflow-model-server-1.5.0/t/tensorflow-model-server/tensorflow-
model-server_1.5.0_all.deb' && \  
dpkg -i "$TEMP_DEB" && \  
rm -f "$TEMP_DEB" && \  
git clone --recurse-submodules https://github.com/tensorflow/serving && \  
mkdir /data  
  
EXPOSE 8888 9000  
WORKDIR /  
VOLUME /data  
  
CMD ["/bin/bash"]  


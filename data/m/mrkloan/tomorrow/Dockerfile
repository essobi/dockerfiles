FROM ubuntu:latest  
LABEL maintainer="Valentin Fries <contact@fries.io>, Vincent Milano
<vincent_mot@hotmail.fr>"  
  
# Install dependencies  
RUN apt-get update &&\  
apt-get install -y\  
# Rust  
vim curl wget g++ git pkg-config\  
# TensorFlow  
python3-numpy python3-dev python3-pip python3-wheel libcupti-dev libssl-dev\  
# kcov  
cmake python\  
libcurl4-openssl-dev libelf-dev libdw-dev\  
libbfd-dev binutils-dev libiberty-dev zlib1g-dev  
  
# Configure Bazel  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" | tee /etc/apt/sources.list.d/bazel.list &&\  
curl https://bazel.build/bazel-release.pub.gpg | apt-key add \- &&\  
apt-get update -y &&\  
apt-get install -y openjdk-8-jdk bazel &&\  
apt-get upgrade -y bazel  
  
# Install TensorFlow python module  
RUN pip3 install tensorflow  
  
# Configure Rust development environment  
RUN curl -sSf https://sh.rustup.rs/ | sh -s -- --default-toolchain nightly -y  
  
# Install kcov  
RUN wget https://github.com/SimonKagstrom/kcov/archive/master.tar.gz &&\  
tar xzf master.tar.gz &&\  
cd kcov-master &&\  
mkdir build &&\  
cd build &&\  
cmake .. &&\  
make &&\  
make install  
  
# Clean image  
RUN apt-get clean &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /tmp/*  
  
# Update PATH and define env variables  
ENV PATH=/root/.cargo/bin:$PATH\  
USER=root\  
TF_CPP_MIN_LOG_LEVEL=2  
# Create a volume containing the indexed crates registry  
VOLUME /root/.cargo/registry


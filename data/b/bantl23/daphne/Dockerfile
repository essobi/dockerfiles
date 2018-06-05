FROM ubuntu:xenial  
  
RUN apt-get update && \  
apt-get install -y \  
wget \  
curl \  
man-db \  
software-properties-common && \  
add-apt-repository ppa:git-core/ppa && \  
echo "deb http://storage.googleapis.com/bazel-apt stable jdk1.8" | tee
/etc/apt/sources.list.d/bazel.list && \  
curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | apt-key
add - && \  
apt-get update && \  
apt-get install -y \  
sudo \  
dpkg-dev \  
ssh \  
iputils-ping \  
vim \  
make \  
gcc \  
g++ \  
gdb \  
cmake \  
automake \  
gcovr \  
lcov \  
git-core \  
ruby \  
python3-pip \  
sqlite3 \  
libboost-all-dev \  
libpython3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libhiredis-dev \  
zlib1g-dev \  
libyaml-dev \  
libcurl4-openssl-dev \  
libffi-dev \  
libreadline-dev \  
librabbitmq-dev \  
libspdlog-dev \  
libsoci-dev \  
python-software-properties \  
rabbitmq-server \  
openjdk-8-jdk \  
ant \  
catch \  
bazel  
  
RUN useradd -m -G sudo docker  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
USER docker  
  
CMD ["/bin/bash"]  


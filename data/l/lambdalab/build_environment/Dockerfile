FROM lambdalab/base  
MAINTAINER lambdalab  
  
ENV LANG en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
  
# RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test  
RUN add-apt-repository -y ppa:git-core/ppa && add-apt-repository -y
ppa:gophers/archive && add-apt-repository -y ppa:ondrej/php  
RUN apt-get update  
  
RUN apt-get install -y sudo  
  
# install python  
RUN apt-get install -y python-pip  
RUN pip install -U pip setuptools  
RUN apt-get install -y python-dev libxml2-dev libxslt-dev  
  
# install ruby  
# RUN curl -sSL https://get.rvm.io | bash  
# RUN echo "source /etc/profile.d/rvm.sh; rvm install ruby-2.0.0-p481; gem
install bundle" | bash  
RUN apt-get install -y ruby  
  
# install zip  
RUN apt-get install -y zip  
  
# ant, maven  
# RUN apt-get install -y ant maven  
# mercurial/hg  
# RUN apt-get install -y mercurial meld  
# install node js  
RUN wget https://nodejs.org/dist/v6.11.3/node-v6.11.3-linux-x64.tar.xz --no-
verbose && tar -xf node-v6.11.3-linux-x64.tar.xz -C /opt && rm
node-v6.11.3-linux-x64.tar.xz  
ENV PATH $PATH:/opt/node-v6.11.3-linux-x64/bin:/usr/lib/go-1.8/bin  
  
# install proto compiler  
RUN apt-get install -y libprotobuf-dev  
#protobuf-compiler  
RUN apt-get install -y protobuf-compiler  
RUN apt-get install -y golang-1.8  
# RUN wget
https://github.com/google/protobuf/releases/download/v3.0.0-beta-3/#
protoc-3.0.0-beta-3-linux-x86_64.zip  
#RUN unzip protoc-3.0.0-beta-3-linux-x86_64.zip -d /opt/protobuf  
#RUN rm protoc-3.0.0-beta-3-linux-x86_64.zip  
#ENV PATH $PATH:/opt/protobuf  
# install thrift  
RUN apt-get install -y libevent-dev automake libtool flex bison pkg-config g++
libssl-dev  
  
# scm  
RUN apt-get install git -y  
  
# php  
RUN apt-get install -y php7.1 php7.1-xml php7.1-mbstring  
  
# help jdk build  
RUN apt-get install -y libcups2-dev libasound2-dev libfreetype6-dev libxtst-
dev libxrender-dev  
  
# install build tool  
RUN apt-get install -y build-essential texinfo libtool bc  
  
# install gcc 5  
# RUN apt-get install -y gcc-5 g++-5 cpp-5 c++-5  
# RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 1  
# RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-5 1  
# RUN update-alternatives --install /usr/bin/cpp cpp /usr/bin/cpp-5 1  
# RUN update-alternatives --install /usr/bin/c++ c++ /usr/bin/c++-5 1  
# install cmake  
RUN wget https://cmake.org/files/v3.8/cmake-3.8.1.tar.gz && tar -xf
cmake-3.8.1.tar.gz && cd cmake-3.8.1 && ./bootstrap && make && make install &&
rm -rf cmake-3.8.1*  
  
# install intel omp so that it's header could be found by clang  
RUN apt-get install -y libiomp-dev  
  
# Hack to get around UID mismatch  
# RUN for i in $(seq 1000 1010); do useradd builder$i -m -u $i -G sudo,root;
done  
# RUN ln -s /root /home/builder0  
RUN echo "%sudo ALL=(ALL) NOPASSWD: /usr/bin/apt-get" >> /etc/sudoers  
  
# Anddroid SDK mount point  
ENV ANDROID_HOME /android-sdk-linux  
RUN apt-get install -y lib32stdc++6 lib32z1  
  
# Others to prevent build failed  
RUN apt-get install -y doxygen ascii  
  
ENV GOROOT /usr/lib/go-1.8  
# TODO: make apt-get need no sudo  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" | tee /etc/apt/sources.list.d/bazel.list  
RUN curl https://bazel.build/bazel-release.pub.gpg | apt-key add -  
RUN apt-get update && apt-get install -y bazel


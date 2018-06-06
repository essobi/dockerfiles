FROM phusion/baseimage:0.10.0  
  
RUN add-apt-repository ppa:beineri/opt-qt-5.10.1-xenial \  
&& apt-get update \  
&& apt-get install wget \  
&& apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-
xenial-6.0 main" \  
&& wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add \- \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends \  
build-essential curl python3 python3-pip python3-setuptools wget \  
qt510base qt510location mesa-common-dev clang-format-6.0 clang-tidy-6.0 \  
&& ln -s /usr/bin/clang-format-6.0 /usr/local/bin/clang-format \  
&& ln -s /usr/bin/clang-tidy-6.0 /usr/local/bin/clang-tidy \  
&& rm /usr/bin/python && ln -s /usr/bin/python3 /usr/bin/python \  
&& cd /tmp \  
&& wget https://cmake.org/files/v3.11/cmake-3.11.0-Linux-x86_64.sh \  
&& chmod a+x cmake-3.11.0-Linux-x86_64.sh \  
&& mkdir /opt/cmake \  
&& sh cmake-3.11.0-Linux-x86_64.sh \--prefix=/opt/cmake --skip-license \  
&& ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake \  
&& pip3 install conan \  
&& conan remote add bincrafters
https://api.bintray.com/conan/bincrafters/public-conan \  
# Clean up APT when done.  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /root/.conan  


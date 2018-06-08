FROM ubuntu:17.10  
ENV abc=hello  
  
RUN apt-get update  
RUN apt-get install -y build-essential  
RUN apt-get install -y libevent-dev  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y git  
RUN apt-get install -y curl  
RUN apt-get install -y golang  
RUN apt-get install -y python  
RUN apt-get install -y librdkafka-dev  
RUN apt-get install -y docker.io  
RUN apt-get install -y sudo  
RUN apt-get install -y python3-pip vim nodejs npm  
RUN apt-get install -y liblzma-dev  
RUN apt-get install -y libunwind-dev  
RUN apt-get install -y libcurl4-openssl-dev libidn11-dev libkrb5-dev
libldap2-dev librtmp-dev libidn2-dev libpsl-dev  
RUN apt-get install -yq \  
git \  
cmake \  
clang-5.0 \  
g++ \  
libcurlpp-dev \  
flex \  
bison \  
libkrb5-dev \  
libsasl2-dev \  
libnuma-dev \  
pkg-config \  
libssl-dev \  
libcap-dev \  
gperf \  
autoconf-archive \  
libevent-dev \  
libtool \  
libboost-all-dev \  
libjemalloc-dev \  
libsnappy-dev \  
wget \  
unzip  
RUN apt-get install -y libgflags-dev  
RUN apt-get install -y libdouble-conversion-dev  
RUN apt-get install -y libgoogle-glog-dev  
RUN pip3 install plumbum pyyaml weka-easypy  
RUN mkdir /usr/local/proxygen  
RUN mkdir /usr/local/include/catch2  
RUN curl -L
https://github.com/catchorg/Catch2/releases/download/v2.1.0/catch.hpp -o
/usr/local/include/catch2/catch.hpp  
RUN curl https://curl.haxx.se/download/curl-7.58.0.tar.gz -o /root/curl.tar.gz  
RUN cd /root && tar -zxf /root/curl.tar.gz && cd curl-7.58.0/ && \  
./configure --enable-optimize --disable-dict --disable-gopher --disable-ftp
--disable-imap --disable-ldap \  
\--disable-ldaps --disable-pop3 --disable-proxy --disable-rtsp --disable-smtp
--disable-telnet --disable-tftp \  
\--disable-zlib --without-ca-bundle --without-gnutls --without-libidn
--without-librtmp --without-libssh2 \  
\--without-nss --without-zlib --disable-psl --without-libidn2 --disable-ba
--disable-shared --without-libpsl \  
\--enable-static && make && make install  
RUN curl -L https://github.com/jpbarrette/curlpp/archive/v0.8.1.tar.gz -o
/root/curlpp.tar.gz  
RUN cd /root && tar -zxf curlpp.tar.gz && cd curlpp-0.8.1 && mkdir build && cd
build && CXXFLAGS=-fPIC CFLAGS=-fPIC cmake make .. -DBUILD_STATIC_LIBS=true &&
make && make install  
RUN curl -L https://github.com/facebook/proxygen/archive/v2018.04.09.00.zip -o
/root/proxygen.zip  
RUN cd /root && unzip proxygen.zip && cd proxygen-2018.04.09.00/proxygen  
ADD deps.sh /root/proxygen-2018.04.09.00/proxygen  
ADD 0001-Control-installation-of-signal-handlers-through-the-.patch
/root/0001-Control-installation-of-signal-handlers-through-the-.patch  
RUN chmod 755 /root/proxygen-2018.04.09.00/proxygen/deps.sh  
RUN git config --global user.email "you@example.com"  
RUN git config --global user.name "Your Name"  
RUN cd /root/proxygen-2018.04.09.00/proxygen && ./deps.sh && ./reinstall.sh  
  
RUN apt-get install -y build-essential fakeroot devscripts apt-src  
ADD build_packages.py /root/build_packages.py  
RUN chmod 755 /root/build_packages.py  
RUN sed -i.bak 's/# deb-src /deb-src /' /etc/apt/sources.list  
RUN apt-get update  
RUN cd /root && /root/build_packages.py openssl  
RUN cd /root && /root/build_packages.py google-glog  
# double-conversion doesn't seem to obey CFLAGS settings  
RUN cd /root && CXX="x86_64-linux-gnu-g++ -fPIC" /root/build_packages.py
double-conversion  
RUN cd /root && /root/build_packages.py lzma  
RUN cd /root && /root/build_packages.py libunwind  
RUN cd /root && dpkg -i *.deb  
  
RUN curl -L https://github.com/gflags/gflags/archive/v2.2.1.tar.gz -o
/root/gflags.tar.gz  
RUN cd /root && tar -zxf gflags.tar.gz && cd gflags-2.2.1 && mkdir build && cd
build && CXXFLAGS=-fPIC CFLAGS=-fPIC cmake .. && make && make install  
  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository ppa:webupd8team/java  
  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
  
RUN apt-get update  
RUN apt-get install -y oracle-java8-installer  
  
RUN add-apt-repository ppa:cwchien/gradle  
RUN apt-get update  
RUN apt-get install -y gradle  
RUN apt-get install -y daemonize  
RUN pip3 install rpyc requests  
  
RUN apt-get build-dep -y grpc  
RUN apt-get build-dep -y c-ares  
RUN apt-get build-dep -y protobuf  
  
RUN cd /root && /root/build_packages.py grpc  
RUN cd /root && /root/build_packages.py c-ares  
RUN cd /root && /root/build_packages.py protobuf  
RUN dpkg -i /root/*grpc*deb  
RUN dpkg -i /root/*protobuf-compiler-grpc*deb  
RUN dpkg -i /root/*protobuf-dev*deb  
RUN dpkg -i /root/*libc-ares2*deb  
  
RUN cd /root && /root/build_packages.py zlib  
RUN rm -f /root/*dbg*  
RUN dpkg -i /root/zlib1g*deb  
  
RUN curl -L http://apache.mivzakim.net/kafka/1.0.0/kafka_2.11-1.0.0.tgz -o
/root/kafka.tar.gz  
RUN cd /root && tar -zxf /root/kafka.tar.gz  
RUN rm /root/*deb /root/*buildinfo /root/*changes /root/*.dsc /root/*.xz  
RUN rm /root/*tar.gz  
RUN mkdir -p /usr/lib/octarine  
  
RUN mkdir /usr/local/include/fake_it  
RUN curl -L
https://raw.githubusercontent.com/eranpeer/FakeIt/2.0.4/single_header/standalone/fakeit.hpp
-o /usr/local/include/fake_it/fakeit.hpp  
  
RUN mkdir /var/lib/docker  
VOLUME /var/lib/docker  
ENV PATH /opt/ldc2/bin:$PATH  


FROM debian:latest  
  
MAINTAINER Dmitrii Zolotov <dzolotov@herzen.spb.ru>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed -i 's~http://httpredir.debian.org~http://mirror.yandex.ru~ig'
/etc/apt/sources.list && \  
apt-get update && apt-get dist-upgrade -y && apt-get install -y uuid-dev clang
libssl-dev libsasl2-dev wget cmake make ruby-dev doxygen ruby valgrind pkg-
config libboost-all-dev libdb5.3++-dev libdb-dev libaio-dev swig libxqilla-dev
libxerces-c-dev libpthread-stubs0-dev libnss3-dev libnspr4-dev python-dev
graphviz help2man krb5-user libgssapi-krb5-2 subversion maven openjdk-7-jdk
python-setuptools sasl2-bin && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN cd /root && mkdir proton && cd proton && wget
https://dist.apache.org/repos/dist/release/qpid/proton/0.17.0/qpid-
proton-0.17.0.tar.gz && tar xzvpf qpid-proton* && \  
cd qpid-proton* && mkdir build && cd build && CXX=clang++ CC=clang cmake
-DCMAKE_CXX_FLAGS=-std=c++11 -DSYSINSTALL_BINDINGS=ON
-DCMAKE_INSTALL_PREFIX=/usr .. && \  
make && make install && rm -rf /root/proton  
  
RUN cd /root && mkdir qpid && cd qpid && wget http://apache-
mirror.rbc.ru/pub/apache/qpid/cpp/1.36.0/qpid-cpp-1.36.0.tar.gz && tar xzvpf
qpid-cpp* && cd qpid-cpp* && \  
mkdir build && cd build && CXX=clang++ CC=clang cmake -DBUILD_TESTING=no
-DBUILD_PROBES=no -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr .. &&
make all && make install && \  
cd /root/qpid && cd qpid-cpp* && cd management/python && ./setup.py build
install && cd ../.. && \  
wget http://apache-mirror.rbc.ru/pub/apache/qpid/python/1.35.0/qpid-
python-1.35.0.tar.gz && tar xzvpf qpid-python* && cd qpid-python* && \  
./setup.py build install && rm -rf /root/qpid  
  
RUN cd /root && mkdir qpid-web && cd qpid-web && svn co
https://svn.apache.org/repos/asf/qpid/branches/0.32/qpid/tools/src/java/ . &&
\  
cd /root/qpid-web && mvn clean package && \  
cd qpid-qmf2-tools/target && mkdir /qmfweb && mv qpid-
qmf2-tools-0.32-bin.tar.gz /qmfweb && cd /qmfweb && \  
tar xzvpf qpid-qmf2-tools-0.32-bin.tar.gz && mv qpid-qmf2-tools/0.32/* . && rm
-rf /root/qpid-web  
  
RUN mkdir /var/log/supervisor/ && mkdir /var/lib/qpidd  
RUN /usr/bin/easy_install supervisor supervisor-stdout supervisor-logging  
ADD supervisord.conf /etc/supervisord.conf  
  
VOLUME ["/var/db/qpidd"]  
  
ADD qpidd.acl /usr/etc/qpid/qpidd.acl.dist  
ADD qpidd.conf /usr/etc/qpid/qpidd.conf.dist  
ADD sasl.conf /usr/etc/sasl2/qpidd.conf  
ADD config.js /qmfweb/bin/qpid-web/web/ui/config.js.dist  
  
ADD runQPID.sh /  
ADD runREST.sh /qmfweb/bin  
  
ENV DOMAIN domain.com  
ENV REALM DOMAIN  
ENV EXTIP 127.0.0.1  
EXPOSE 5672 8080  
CMD ["supervisord","-n","-c","/etc/supervisord.conf"]  


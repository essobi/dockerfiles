FROM ubuntu:xenial  
MAINTAINER Jos Hendriks <jos@hendriks.software>  
  
ENV HOME /bitcoin  
  
# add user with specified (or default) user/group ids  
#ENV USER_ID ${USER_ID:-1000}  
#ENV GROUP_ID ${GROUP_ID:-1000}  
  
ENV PROJECT arcticcoin  
ENV GIT_URL git://github.com/ArcticCore/arcticcoin.git  
ENV SVC_VERSION tags/v0.12.1.2  
ENV HOME_DIR /usr/local/bin  
ENV NODE_PORT 7209  
ENV RPC_PORT 7208  
  
# install system packages and compile  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install --no-install-recommends file icu-devtools libboost-
atomic1.58.0 \  
libboost-chrono1.58.0 libboost-context1.58.0 libboost-coroutine1.58.0
libboost-date-time1.58.0 \  
libboost-filesystem1.58.0 libboost-graph-parallel1.58.0 libboost-graph1.58.0 \  
libboost-iostreams1.58.0 libboost-locale1.58.0 libboost-mpi-python1.58.0
libboost-mpi1.58.0 \  
libboost-program-options1.58.0 libboost-python1.58.0 libboost-random1.58.0
libboost-regex1.58.0 \  
libboost-serialization1.58.0 libboost-signals1.58.0 libboost-system1.58.0
libboost-test1.58.0 \  
libboost-thread1.58.0 libboost-timer1.58.0 libboost-wave1.58.0 libc-dev-bin
libdb5.3++ libevent-2.0-5 \  
libevent-core-2.0-5 libevent-extra-2.0-5 libevent-openssl-2.0-5 libevent-
pthreads-2.0-5 \  
libgmpxx4ldbl libhwloc5 libibverbs1 libicu55 libltdl7 libmagic1 libnuma1 \  
libopenmpi1.10 libprotobuf-lite9v5 libprotobuf9v5 libpython-stdlib
libpython2.7 \  
libpython2.7-minimal libpython2.7-stdlib linux-libc-dev mime-support \  
mpi-default-bin openmpi-bin openmpi-common python python-minimal python2.7
python2.7-minimal \  
&& apt-get -y install --no-install-recommends build-essential libtool
autotools-dev \  
libcurl4-openssl-dev libboost-all-dev libssl-dev libdb++-dev make autoconf
automake \  
libtool git apt-utils libprotobuf-dev pkg-config libboost-filesystem-dev
libboost-chrono-dev \  
libevent-dev libboost-program-options-dev libgmp-dev libboost-test-dev
libboost-thread-dev \  
&& mkdir -p /opt/code/ && cd /opt/code/ && git clone ${GIT_URL} ${PROJECT} \  
&& cd /opt/code/${PROJECT} && git checkout ${SVC_VERSION} \  
&& ./autogen.sh && ./configure --enable-tests=no --with-incompatible-bdb \  
\--enable-glibc-back-compat --with-gui=no \  
CFLAGS="-march=native" LIBS="-lcurl -lssl -lcrypto -lz" \  
&& make && make install \  
&& apt-get -y remove build-essential \  
libboost-all-dev libboost-atomic-dev libboost-atomic1.58-dev \  
libboost-chrono-dev libboost-chrono1.58-dev \  
libboost-context-dev libboost-context1.58-dev \  
libboost-coroutine-dev libboost-coroutine1.58-dev \  
libboost-date-time-dev libboost-date-time1.58-dev \  
libboost-dev libboost-exception-dev libboost-exception1.58-dev \  
libboost-filesystem-dev libboost-filesystem1.58-dev \  
libboost-graph-dev libboost-graph-parallel-dev \  
libboost-graph-parallel1.58-dev libboost-graph1.58-dev \  
libboost-iostreams-dev libboost-iostreams1.58-dev libboost-locale-dev \  
libboost-locale1.58-dev libboost-log-dev \  
libboost-log1.58-dev libboost-log1.58.0 libboost-math-dev \  
libboost-math1.58-dev libboost-math1.58.0 libboost-mpi-dev \  
libboost-mpi-python-dev libboost-mpi-python1.58-dev \  
libboost-mpi1.58-dev libboost-program-options-dev \  
libboost-program-options1.58-dev libboost-python-dev \  
libboost-python1.58-dev libboost-random-dev libboost-random1.58-dev \  
libboost-regex-dev libboost-regex1.58-dev libboost-serialization-dev \  
libboost-serialization1.58-dev libboost-signals-dev libboost-signals1.58-dev \  
libboost-system-dev libboost-system1.58-dev libboost-test-dev libboost-
test1.58-dev \  
libboost-thread-dev libboost-thread1.58-dev libboost-timer-dev libboost-
timer1.58-dev \  
libboost-tools-dev libboost-wave-dev libboost-wave1.58-dev libboost1.58-dev \  
libboost1.58-tools-dev libc6-dev libdb5.3++-dev libdb5.3-dev libevent-dev \  
libexpat1-dev libgmp-dev libibverbs-dev libicu-dev libltdl-dev libnuma-dev \  
libopenmpi-dev libprotobuf-dev libpython-dev libpython2.7-dev libssl-dev \  
mpi-default-dev python-dev python2.7-dev zlib1g-dev \  
&& apt -y autoremove \  
&& rm -rf /opt/code \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE ${NODE_PORT} ${RPC_PORT}  
  
COPY start.sh /start.sh  
RUN chmod 777 /start.sh  
CMD /start.sh


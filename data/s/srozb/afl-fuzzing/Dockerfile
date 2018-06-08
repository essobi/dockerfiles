FROM phusion/baseimage:0.9.19  
MAINTAINER Slawomir Rozbicki <docker@rozbicki.eu>  
  
# Specify program  
ENV PROG afl-fuzz  
ENV VER 2.19b  
# Specify source extension  
ENV EXT tgz  
# Install directory  
ENV PREFIX /opt/afl-fuzz  
# Path should include prefix  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PREFIX/bin  
  
RUN apt-get update -y && apt-get install -y gcc cmake make libtool-bin wget \  
python automake bison libglib2.0 git libssl-dev nettle-dev  
  
# Get sources  
WORKDIR /usr/src/  
RUN curl -o afl-$VER.tgz http://lcamtuf.coredump.cx/afl/releases/afl-$VER.tgz
\  
&& tar -xzf afl-$VER.tgz && git clone https://github.com/iagox86/dnsmasq-
fuzzing.git  
  
# Build afl-fuzz  
WORKDIR /usr/src/afl-$VER  
RUN make && make install  
  
# Build afl-fuzz qemu-mode  
WORKDIR /usr/src/afl-$VER/qemu_mode  
RUN ./build_qemu_support.sh && mkdir -p $PREFIX/in -p $PREFIX/out  
  
# Build dnsmasq w/ fuzzing support  
WORKDIR /usr/src/dnsmasq-fuzzing  
RUN CC=/opt/afl-fuzz/bin/afl-gcc CFLAGS=-DFUZZ make  
  
WORKDIR $PREFIX  
  
RUN echo "CC=/opt/afl-fuzz/bin/afl-gcc" >> /root/.bashrc \  
&& echo "CXX=/opt/afl-fuzz/bin/afl-g++" >> /root/.bashrc  
  
ADD fuzz_random.sh /opt/afl-fuzz/  
ADD afl-fuzz-parallel /opt/afl-fuzz/bin/  
CMD ["/opt/afl-fuzz/fuzz_random.sh"]  
  


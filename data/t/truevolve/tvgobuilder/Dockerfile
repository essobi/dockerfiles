FROM ubuntu:16.04  
RUN sed -i "s/^deb /deb \\[arch=$(dpkg --print-architecture)] /"
/etc/apt/sources.list  
RUN for SUFFIX in "" "-updates" "-security"; do \  
echo "deb [arch=armhf] http://ports.ubuntu.com/ubuntu-ports/ xenial${SUFFIX}
main restricted universe multiverse" \  
>> /etc/apt/sources.list.d/armhf.list; \  
done  
RUN dpkg --add-architecture armhf  
  
# gcc for cgo  
RUN apt-get update && apt-get install -y \  
build-essential \  
autotools-dev \  
libssl-dev \  
dh-autoreconf \  
opensc \  
opensc-pkcs11 \  
g++ \  
gcc \  
libc6-dev \  
make \  
curl \  
libpcre3-dev \  
vim \  
git \  
sudo \  
gcc-arm-linux-gnueabihf \  
g++-arm-linux-gnueabihf \  
libusb++-dev \  
libltdl-dev \  
libltdl-dev:armhf \  
sudo  
  
RUN mkdir /tmp/swig/  
COPY swig.tar.gz /tmp/swig/  
RUN tar -C /tmp/swig/ --strip-components=1 -xzf /tmp/swig/swig.tar.gz \  
&& cd /tmp/swig/ \  
&& ./configure \  
&& make \  
&& make install  
  
RUN mkdir -p /home/developer/ && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown developer:developer -R /home/developer  
  
USER developer  
  
ENV GOLANG_VERSION 1.9.2  
WORKDIR /home/developer/  
COPY go1.9.2.linux-amd64.tar.gz /home/developer/golang.tar.gz  
  
RUN tar -C /home/developer/ -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOROOT /home/developer/go  
ENV GOPATH /home/developer/  
ENV PATH $GOROOT/bin:$PATH  
  
WORKDIR $GOPATH  
  
CMD /bin/bash  


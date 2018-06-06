# Stage: iproute2  
FROM ubuntu:16.10 as iproute2  
WORKDIR /tmp  
RUN apt-get update && apt-get install -y --no-install-recommends gcc git pkg-
config libc6-dev.i386 bison flex binutils  
RUN git clone -b v4.10.0
git://git.kernel.org/pub/scm/linux/kernel/git/shemminger/iproute2.git  
WORKDIR /tmp/iproute2  
RUN ./configure  
RUN make -j `getconf _NPROCESSORS_ONLN`  
RUN strip -s tc/tc  
RUN strip -s ip/ip  
  
# Stage: clang  
FROM ubuntu:16.10 as clang  
WORKDIR /tmp  
ADD clang-3.8.1.key .  
RUN apt-get update && apt-get install -y --no-install-recommends curl xz-utils
binutils  
RUN gpg --import /tmp/clang-3.8.1.key  
RUN curl -Ssl -o clang+llvm.tar.xz
http://releases.llvm.org/3.8.1/clang+llvm-3.8.1-x86_64-linux-gnu-
ubuntu-16.04.tar.xz  
RUN curl -Ssl -o clang+llvm.tar.xz.sig
http://releases.llvm.org/3.8.1/clang+llvm-3.8.1-x86_64-linux-gnu-
ubuntu-16.04.tar.xz.sig  
RUN gpg --verify clang+llvm.tar.xz.sig  
RUN mkdir -p /usr/local  
RUN tar -C /usr/local -xJf ./clang+llvm.tar.xz  
RUN mv /usr/local/clang+llvm-3.8.1-x86_64-linux-gnu-ubuntu-16.04
/usr/local/clang+llvm  
RUN rm clang+llvm.tar.xz  
RUN rm -fr /usr/local/clang+llvm/include/llvm-c  
RUN rm -fr /usr/local/clang+llvm/include/clang-c  
RUN rm -fr /usr/local/clang+llvm/include/c++  
RUN rm -fr /usr/local/clang+llvm/share  
RUN ls -d /usr/local/clang+llvm/lib/* | grep -vE clang$ | xargs rm -r  
RUN ls -d /usr/local/clang+llvm/bin/* | grep -vE "clang$|clang-3.8$|llc$" |
xargs rm -r  
RUN ls -d /usr/local/clang+llvm/bin/* | xargs strip -s  
  
# Stage: bpf-map  
FROM ubuntu:16.10 as bpf-map  
WORKDIR /tmp  
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-
certificates  
RUN curl -sS -L https://github.com/cilium/bpf-map/releases/download/v1.0/bpf-
map -o bpf-map  
RUN chmod +x bpf-map  
  
# Stage: CNI  
FROM ubuntu:16.10 as cni  
WORKDIR /tmp  
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-
certificates binutils  
RUN curl -sS -L https://storage.googleapis.com/kubernetes-release/network-
plugins/cni-0799f5732f2a11b329d9e3d51b9c8f2e3759f2ff.tar.gz -o cni.tar.gz  
RUN tar -xvf cni.tar.gz  
RUN strip -s bin/loopback  
  
# Stage: gops  
FROM golang:1.9 as gops  
WORKDIR /tmp  
RUN go get -u github.com/jteeuwen/go-bindata/...  
RUN go get -u github.com/google/gops  
  
# Final stage: runtime  
FROM ubuntu:16.10  
# Use of alpine is not possible right now due to use of clang/llc which  
#FROM alpine:3.5  
#FROM frolvlad/alpine-glibc  
LABEL maintainer="maintainer@cilium.io"  
WORKDIR /bin  
COPY \--from=iproute2 /tmp/iproute2/tc/tc /tmp/iproute2/ip/ip /bin/  
COPY \--from=bpf-map /tmp/bpf-map .  
COPY \--from=gops /go/bin/gops .  
WORKDIR /usr/local/clang+llvm  
COPY \--from=clang /usr/local/clang+llvm .  
WORKDIR /cni/bin  
COPY \--from=cni /tmp/bin/loopback .  


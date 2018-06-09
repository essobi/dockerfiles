FROM ubuntu:17.10 AS build  
COPY scripts/installtools.sh .  
RUN apt-get update && \  
apt-get install -y \  
apt-utils pkg-config \  
git mercurial \  
build-essential clang \  
libffi-dev libftdi-dev \  
graphviz xdot gperf \  
gawk tclsh tcl-dev \  
libreadline-dev bison \  
flex python autoconf && \  
./installtools.sh  
  
FROM ubuntu:17.10  
COPY --from=build /root/fpga/out /  
RUN mkdir -p /root/fpga/out/lib/ && \  
ln -s /lib/ivl /root/fpga/out/lib/ivl && \  
apt-get update && \  
apt-get install -y --no-install-recommends make perl tclsh && \  
apt-get autoremove -yqq && \  
apt-get autoclean -yqq && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt


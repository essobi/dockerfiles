FROM centos:7  
# Install dependencies  
RUN yum update -y && yum install -y epel-release && \  
yum install -y libaio-devel leveldb-devel snappy-devel libcap-devel
libseccomp-devel \  
gcc-c++ make git golang jq which openssl  
  
# Build stenographer  
ENV GOPATH=/go  
RUN go get github.com/google/stenographer  
  
# Build stenotype  
WORKDIR /go/src/github.com/google/stenographer  
RUN make -C stenotype  
  
# Create user  
RUN adduser --system --no-create-home stenographer  
  
# Configuration directory  
RUN mkdir -p /etc/stenographer/certs  
RUN chown -R stenographer:stenographer /etc/stenographer  
  
# Data directory  
RUN mkdir /data  
RUN chown stenographer:stenographer /data  
  
# Install example config  
RUN install ./configs/steno.conf /etc/stenographer/config  
  
# Install executables  
RUN install -t /usr/bin stenotype/stenotype  
RUN install -t /usr/bin stenoread  
RUN install -t /usr/bin stenocurl  
RUN install -t /usr/bin stenokeys.sh  
  
# Set compabilities for stenotype  
RUN setcap 'CAP_NET_RAW+ep CAP_NET_ADMIN+ep CAP_IPC_LOCK+ep'
/usr/bin/stenotype  
  
ENV PATH=$PATH:$GOPATH/bin  
  
USER stenographer  
  
CMD stenokeys.sh stenographer stenographer && stenographer -syslog=false  


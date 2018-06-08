FROM centos:latest  
  
# Install Dependencies  
RUN yum -y install epel-release  
RUN yum install -y tcpdump sudo libaio-devel leveldb-devel snappy-devel
libcap-devel libseccomp-devel \  
gcc-c++ make git golang jq which openssl  
  
ENV GOPATH=/go  
  
# Build and set permissions  
RUN go get github.com/google/stenographer && \  
cd /go/src/github.com/google/stenographer && \  
go build && \  
make -C stenotype && \  
adduser --system \--no-create-home stenographer && \  
#sudo cp -v configs/limits.conf /etc/security/limits.d/stenographer.conf && \  
mkdir /etc/stenographer /etc/stenographer/certs /data /data/stenographer
/data/stenographer/logs /data/stenographer/index && \  
chown -R root:root /etc/stenographer/certs && \  
chown -R stenographer:stenographer /data/stenographer  
  
# Copy over default config  
COPY etc/config /etc/stenographer/config  
  
# Generate keys and copy executables  
RUN chmod 644 /etc/stenographer/config && \  
cd /go/src/github.com/google/stenographer && \  
./stenokeys.sh stenographer stenographer && \  
install -t /usr/bin stenotype/stenotype && \  
install -t /usr/bin stenocurl && \  
install -t /usr/bin stenoread && \  
install -t /usr/bin stenographer && \  
setcap 'CAP_NET_RAW+ep CAP_NET_ADMIN+ep CAP_IPC_LOCK+ep' /usr/bin/stenotype  
  
# Run as user stenographer  
USER stenographer  
  
# Make sure the port matches the config  
EXPOSE 1234  
  
CMD ["stenographer", "-syslog=false"]  


FROM coquelux/apachephp  
  
ENV GOLANG_TAG go1.4.2  
ENV TRANSPORTER_TAG v0.1.1  
  
RUN apt-get install -y gcc libc6-dev make \--no-install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH /go/bin:/opt/go/bin:$PATH  
ENV GOPATH /go  
  
# Install go  
RUN cd /opt && \  
git clone --branch $GOLANG_TAG --depth 1 https://go.googlesource.com/go && \  
cd go/src && \  
./all.bash  
  
# Install godep  
RUN go get github.com/tools/godep  
  
# Install transporter  
RUN mkdir -p /go/src/github.com/compose /go/bin /go/pkg && \  
cd /go/src/github.com/compose && \  
git clone --branch $TRANSPORTER_TAG --depth 1
https://github.com/compose/transporter.git && \  
cd transporter && \  
godep restore && \  
godep go build -a ./cmd/... && \  
mv transporter /go/bin/  


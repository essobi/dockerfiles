###############################################################################  
# roboll/cfssl-sidecar  
###############################################################################  
FROM sdurrheimer/alpine-glibc  
  
RUN apk update && apk add \  
libltdl \  
&& rm -rf /var/cache/apk/*  
  
COPY . /go/src/github.com/roboll/cfssl-sidecar  
  
RUN buildDeps=' \  
go \  
git \  
gcc \  
libc-dev \  
libtool \  
libgcc \  
' \  
set -x && \  
apk update && \  
apk add $buildDeps && \  
cd /go/src/github.com/roboll/cfssl-sidecar && \  
export GOPATH=/go && \  
go get github.com/tools/godep && /go/bin/godep restore && \  
go build -o /cfssl-sidecar . && \  
apk del $buildDeps && \  
rm -rf /var/cache/apk/* && \  
rm -rf /go && \  
echo "Build complete."  
  
ENTRYPOINT ["/cfssl-sidecar"]  


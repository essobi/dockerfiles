FROM alpine  
  
ARG project_dir=/gowork/src/github.com/danielpanteleit/local-btrfs  
ARG go_archive=go1.8.linux-amd64.tar.gz  
  
COPY *.go $project_dir/  
COPY daemon $project_dir/daemon/  
COPY cli $project_dir/cli/  
COPY vendor/vendor.json $project_dir/vendor/  
  
RUN apk add --no-cache -t build wget tar gzip ca-certificates git && \  
: ---- && \  
wget https://storage.googleapis.com/golang/$go_archive && \  
tar xf $go_archive && \  
mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2
&& \  
rm $go_archive && \  
: ---- && \  
export GOROOT=/go && \  
export GOPATH=/gowork && \  
export PATH=/go/bin:/gowork/bin:$PATH && \  
: ---- && \  
go get -u github.com/kardianos/govendor && \  
cd $project_dir && \  
govendor sync -v && \  
: ---- && \  
go build -o /local-btrfs -v && \  
cd / && \  
: ---- && \  
rm -rf go gowork && \  
apk del --no-cache build && \  
apk add --no-cache btrfs-progs  
  
ENTRYPOINT ["/local-btrfs"]  
  
CMD ["daemon"]  


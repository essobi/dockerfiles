FROM golang:1.10-alpine3.7 as builder  
  
ENV VERSION=0.3.5  
ENV IPFS_GX_USE_GLOBAL=1  
RUN apk add --no-cache --virtual .build-deps \  
build-base \  
git  
  
# Get source  
RUN mkdir -p $GOPATH/src/github.com/ipfs && \  
git clone \--depth 1 --branch v$VERSION https://github.com/ipfs/ipfs-cluster
$GOPATH/src/github.com/ipfs/ipfs-cluster  
  
# Replace g, gx-go  
# Disable Makefile gx, gx-go installation  
RUN cd $GOPATH/src/github.com/ipfs/ipfs-cluster && \  
go get -v -u github.com/whyrusleeping/gx github.com/whyrusleeping/gx-go && \  
sed -i 's/gx:.*/gx:/' Makefile && \  
mkdir -p deptools && \  
rm -rf deptools/gx_* deptools/gx-go_* && \  
ln -s $(which gx) deptools/gx_$(cat Makefile | grep gx_version= | tr '=' ' ' |
awk '{print $2}') && \  
ln -s $(which gx-go) deptools/gx-go_$(cat Makefile | grep gx-go_version= | tr
'=' ' ' | awk '{print $2}')  
  
# Build  
RUN cd $GOPATH/src/github.com/ipfs/ipfs-cluster && \  
make build && \  
mv ipfs-cluster-ctl/ipfs-cluster-ctl $GOPATH/bin/ipfs-cluster-ctl && \  
mv ipfs-cluster-service/ipfs-cluster-service $GOPATH/bin/ipfs-cluster-service  
  
###  
FROM alpine:3.7  
ENV IPFS_CLUSTER_PATH /data/ipfs-cluster  
  
# Ports for  
EXPOSE 9094  
EXPOSE 9095  
EXPOSE 9096  
ENTRYPOINT ["tini", "--", "/usr/local/bin/entrypoint.sh"]  
# Execute the daemon subcommand by default  
CMD ["daemon", "--upgrade"]  
  
RUN apk add --no-cache --virtual .run-deps \  
ca-certificates \  
tini \  
su-exec && \  
mkdir -p $IPFS_CLUSTER_PATH && \  
adduser -D -h $IPFS_CLUSTER_PATH -u 1000 -G users ipfs && \  
chown ipfs:users $IPFS_CLUSTER_PATH  
  
VOLUME $IPFS_CLUSTER_PATH  
  
COPY \--from=builder /go/bin/ipfs-cluster-ctl /usr/local/bin/ipfs-cluster-ctl  
COPY \--from=builder /go/bin/ipfs-cluster-service /usr/local/bin/ipfs-cluster-
service  
COPY \--from=builder /go/src/github.com/ipfs/ipfs-cluster/docker/entrypoint.sh
/usr/local/bin/entrypoint.sh  


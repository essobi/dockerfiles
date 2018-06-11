FROM golang:1.10-alpine3.7 as builder  
  
ENV VERSION=0.4.14  
ENV IPFS_GX_USE_GLOBAL=1  
RUN apk add --no-cache --virtual .build-deps \  
build-base \  
git  
  
# Get source  
RUN mkdir -p $GOPATH/src/github.com/ipfs && \  
git clone \--depth 1 --branch v$VERSION https://github.com/ipfs/go-ipfs
$GOPATH/src/github.com/ipfs/go-ipfs  
  
# Replace g, gx-go  
RUN cd $GOPATH/src/github.com/ipfs/go-ipfs && \  
go get -v -u github.com/whyrusleeping/gx github.com/whyrusleeping/gx-go && \  
rm -rf bin/gx bin/gx-go && \  
ln -s $(which gx) bin/gx && \  
ln -s $(which gx-go) bin/gx-go  
  
RUN cd $GOPATH/src/github.com/ipfs/go-ipfs && \  
make build  
  
###  
FROM alpine:3.7  
# The default logging level  
ENV IPFS_LOGGING ""  
ENV IPFS_PATH /data/ipfs  
  
# Ports for Swarm TCP, Swarm uTP, API, Gateway, Swarm Websockets  
EXPOSE 4001  
EXPOSE 4002/udp  
EXPOSE 5001  
EXPOSE 8080  
EXPOSE 8081  
# This just makes sure that:  
# 1. There's an fs-repo, and initializes one if there isn't.  
# 2. The API and Gateway are accessible from outside the container.  
ENTRYPOINT ["tini", "--", "/usr/local/bin/start_ipfs"]  
# Execute the daemon subcommand by default  
CMD ["daemon", "--migrate=true"]  
  
# Create the fs-repo directory and switch to a non-privileged user.  
RUN apk add --no-cache --virtual .run-deps \  
ca-certificates \  
tini \  
su-exec \  
fuse && \  
mkdir -p $IPFS_PATH /ipfs /ipns && \  
addgroup fuse && \  
adduser -D -h $IPFS_PATH -u 1000 -G users ipfs && \  
addgroup ipfs fuse && \  
chown ipfs:users $IPFS_PATH /ipfs /ipns  
  
# Expose the fs-repo as a volume.  
# start_ipfs initializes an fs-repo if none is mounted.  
# Important this happens after the USER directive so permission are correct.  
VOLUME $IPFS_PATH  
  
COPY \--from=builder /go/src/github.com/ipfs/go-ipfs/cmd/ipfs/ipfs
/usr/local/bin/ipfs  
COPY \--from=builder /go/src/github.com/ipfs/go-ipfs/bin/container_daemon
/usr/local/bin/start_ipfs  


FROM golang:1.9.2-alpine3.6  
RUN apk update && \  
apk upgrade && \  
apk add git make socat build-base  
  
ENV PS1="$(whoami)@$(hostname):$(pwd)$ " \  
HOME="/root" \  
TERM="xterm"  
RUN go-wrapper download -u github.com/NebulousLabs/Sia/...  
RUN go-wrapper download -u github.com/bgentry/speakeasy  
RUN cd /go/src/github.com/NebulousLabs/Sia && \  
git checkout -b v1.3.0 tags/v1.3.0 && \  
make release-std  
  
RUN go-wrapper download -u github.com/minio/minio  
#RUN go-wrapper download -u github.com/mattn/go-sqlite3  
#RUN go-wrapper download -u github.com/boltdb/bolt  
WORKDIR /go/src/github.com/minio/minio  
  
ENV REFRESHED_AT 29.8.17  
RUN cd /go/src/github.com/minio/minio && \  
git remote add dvstate https://github.com/dvstate/minio.git && \  
git fetch dvstate && \  
git checkout -b sia_integration_v2 dvstate/sia_integration_v2 && \  
make install  
  
RUN apk del --purge  
  
EXPOSE 9000  
ENTRYPOINT minio gateway sia 192.168.1.99:9980  


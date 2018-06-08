FROM golang:alpine  
RUN apk --update add git ca-certificates  
ENV CGO_ENABLED 0  
COPY . /go/src/github.com/fkautz/tigerbat  
RUN go get -v github.com/fkautz/tigerbat  
ENV UPSTREAM_SERVER http://www.example.com  
ENV ETCD http://etcd:2379  
EXPOSE 80 8000  
RUN mkdir data  
CMD tigerbat server --address=0.0.0.0:80 --mirror-url=${UPSTREAM_SERVER}
\--peering-address=http://${HOSTNAME}:8080 --etcd=${ETCD}  


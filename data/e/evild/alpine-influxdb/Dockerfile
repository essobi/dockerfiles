  
FROM evild/alpine-base:1.0.0  
MAINTAINER Dominique HAAS <contact@dominique-haas.fr>  
  
ENV INFLUXDB_VERSION 0.11.0  
ENV GOPATH /go  
  
RUN \  
build_pkgs="curl go git mercurial" \  
&& apk --no-cache add ${build_pkgs} \  
&& mkdir -p ${GOPATH}/src/github.com/influxdata && cd
${GOPATH}/src/github.com/influxdata \  
&& git clone https://github.com/influxdata/influxdb.git \  
&& go get -u -f -t ./... \  
&& go build -ldflags="-X main.version=v${INFLUXDB_VERSION} -X
main.branch=master -X main.commit=`cd influxdb && git rev-parse HEAD`" ./... \  
&& go install ./... \  
&& cp $GOPATH/bin/* /usr/local/bin \  
&& go clean -i -r \  
&& apk del ${build_pkgs} \  
&& rm -rf ${GOPATH} /tmp/* /var/cache/apk/* /root/.n*  
  
ADD ./config.toml /usr/share/influxdb/config.toml  
ADD root /  
  
VOLUME ["/data"]  
  
EXPOSE 8083  
EXPOSE 8086  
# Raft port (for clustering, don't expose)  
# EXPOSE 8090  
# Protobuf port (flor clustering, don't expose)  
# EXPOSE 8099  


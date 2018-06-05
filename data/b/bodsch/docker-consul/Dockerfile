  
FROM golang:1.10-alpine as builder  
  
ARG BUILD_DATE  
ARG BUILD_TYPE  
ARG CONSUL_VERSION  
  
#
---------------------------------------------------------------------------------------  
RUN \  
apk update --no-cache && \  
apk upgrade \--no-cache && \  
apk add \  
bash git make zip  
  
RUN \  
export GOPATH=/opt/go && \  
echo "get sources ..." && \  
go get github.com/hashicorp/consul || true && \  
cd ${GOPATH}/src/github.com/hashicorp/consul && \  
if [ "${BUILD_TYPE}" == "stable" ] ; then \  
echo "switch to stable Tag v${CONSUL_VERSION}" && \  
git checkout tags/v${CONSUL_VERSION} 2> /dev/null ; \  
fi  
  
RUN \  
export GOPATH=/opt/go && \  
export PATH=${GOPATH}/bin:${PATH} && \  
cd ${GOPATH}/src/github.com/hashicorp/consul && \  
export GOMAXPROCS=4 && \  
make && \  
cp -v bin/consul /usr/bin/  
  
CMD ["/bin/bash"]  
  
#
---------------------------------------------------------------------------------------  
FROM alpine:3.7  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
LABEL \  
version="1804" \  
maintainer="Bodo Schulz <bodo@boone-schulz.de>" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="Consul Docker Image" \  
org.label-schema.description="Inofficial Consul Docker Image" \  
org.label-schema.url="https://www.consul.io/" \  
org.label-schema.vcs-url="https://github.com/bodsch/docker-consul" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.version=${CONSUL_VERSION} \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="GNU Lesser General Public License v2.1"  
  
COPY \--from=builder /usr/bin/consul /usr/bin/consul  
  
VOLUME [ "/data" ]  
  
ENTRYPOINT [ "/usr/bin/consul" ]  
  
CMD [ "agent", "-data-dir", "/data" ]  
  
#
---------------------------------------------------------------------------------------  


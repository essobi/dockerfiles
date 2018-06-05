  
FROM golang:1.10-alpine as builder  
  
ARG BUILD_DATE  
ARG BUILD_TYPE  
ARG VAULT_VERSION  
  
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
go get github.com/hashicorp/vault || true && \  
cd ${GOPATH}/src/github.com/hashicorp/vault && \  
if [ "${BUILD_TYPE}" == "stable" ] ; then \  
echo "switch to stable Tag v${VAULT_VERSION}" && \  
git checkout tags/v${VAULT_VERSION} 2> /dev/null ; \  
fi  
  
RUN \  
export GOPATH=/opt/go && \  
export PATH=${GOPATH}/bin:${PATH} && \  
cd ${GOPATH}/src/github.com/hashicorp/vault && \  
export GOMAXPROCS=4 && \  
make bootstrap && \  
make && \  
cp -v bin/vault /usr/bin/  
  
CMD ["/bin/bash"]  
  
#
---------------------------------------------------------------------------------------  
FROM alpine:3.7  
  
EXPOSE 8200  
  
LABEL \  
version="1804" \  
maintainer="Bodo Schulz <bodo@boone-schulz.de>" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="Vault Docker Image" \  
org.label-schema.description="Inofficial Vault Docker Image" \  
org.label-schema.url="https://www.vaultproject.io/" \  
org.label-schema.vcs-url="https://github.com/bodsch/docker-vault" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.version=${VAULT_VERSION} \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="GNU Lesser General Public License v2.1"  
#
---------------------------------------------------------------------------------------  
  
COPY \--from=builder /usr/bin/vault /usr/bin/vault  
  
ENTRYPOINT [ "/usr/bin/vault" ]  
  
CMD [ "version" ]  
  
#
---------------------------------------------------------------------------------------  


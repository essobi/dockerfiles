# build stage  
FROM golang:1.9.0 AS build-env  
ADD . /go/src/github.com/kedgeproject/json-schema-generator  
RUN export GOBIN=$GOPATH/bin && cd /go/src/github.com/kedgeproject/json-
schema-generator && make install  
  
# final stage  
FROM fedora:27  
RUN dnf install -y --setopt=tsflags=nodocs npm python-pip && \  
dnf clean all && \  
npm install -g api-spec-converter --unsafe-perm=true \--allow-root && \  
pip install openapi2jsonschema  
  
COPY ./scripts/entrypoint.sh /usr/local/sbin/  
  
COPY \--from=build-env /go/bin/schemagen /usr/local/sbin/  
  
WORKDIR /data  
  
CMD ["entrypoint.sh", "--strict"]  
  


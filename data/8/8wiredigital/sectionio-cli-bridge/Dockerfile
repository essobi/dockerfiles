FROM golang:1.7.4-alpine3.5  
MAINTAINER 8 Wire Digital <info@8wiredigital.co.nz>  
  
ENV SRC_DIR=/tmp/src \  
BUILD_DEPS="git" \  
PERSISTANT_DEPS=""  
ADD ./ $SRC_DIR/varnish-cli-bridge  
  
RUN apk --update add ${PERSISTANT_DEPS} ${BUILD_DEPS} \  
&& mkdir -p ${SRC_DIR} \  
&& cd ${SRC_DIR}/varnish-cli-bridge \  
&& go test ./ || { echo 'Failed to compile and test.' ; exit 1; } \  
&& CGO_ENABLED=0 GOOS=linux go build -a -ldflags "-X main.version=$(git
describe --abbrev=0 --tags) -X main.commitHash=$(git rev-parse HEAD)" -tags
netgo \  
&& mv varnish-cli-bridge /usr/bin \  
&& rm -rf ${SRC_DIR}  
  
EXPOSE 6082  
CMD ["varnish-cli-bridge"]  


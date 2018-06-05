FROM carml/go-caffe2:amd64-gpu-latest  
MAINTAINER Abdul Dakkak <dakkak@illinois.edu>  
  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VCS_URL  
ARG VERSION  
LABEL org.caffe2.agent.build-date=$BUILD_DATE \  
org.caffe2.agent.name="caffe2 agent" \  
org.caffe2.agent.description="" \  
org.caffe2.agent.url="https://www.carml.org/" \  
org.caffe2.agent.vcs-ref=$VCS_REF \  
org.caffe2.agent.vcs-url=$VCS_URL \  
org.caffe2.agent.vendor="CarML" \  
org.caffe2.agent.version=$VERSION \  
org.caffe2.agent.schema-version="1.0"  
  
# Get Go bindings  
ENV PKG github.com/rai-project/caffe2  
WORKDIR $GOPATH/src/$PKG  
  
RUN git clone \--depth=1 --branch=master https://${PKG}.git . && \  
glide install && \  
rm -fr vendor/github.com/Sirupsen && \  
find vendor -type f -exec sed -i 's/Sirupsen/sirupsen/g' {} + && \  
go build -a -installsuffix cgo -ldflags "-s -w -X ${PKG}/Version=${VERSION} -X
${PKG}/GitCommit=${VCS_REF} -X ${PKG}/BuildDate=${BUILD_DATE}"&& \  
cd caffe2-agent && \  
go install && \  
cd .. && \  
rm -fr vendor  
  
ENTRYPOINT ["caffe2-agent", "--debug", "--verbose"]  


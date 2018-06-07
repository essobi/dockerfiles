FROM golang:1.8  
  
ENV GLIDE_VER v0.12  
  
RUN set -x && \  
go get github.com/Masterminds/glide && \  
cd ${GOPATH}/src/github.com/Masterminds/glide && \  
TAG=$(git tag | grep ${GLIDE_VER} | sort | tail -1) && \  
git checkout ${TAG} && \  
go install  


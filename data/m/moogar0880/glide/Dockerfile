FROM golang:1.8-alpine  
  
LABEL maintainer "moogar0880@gmail.com"  
  
RUN apk --update upgrade && \  
apk add make git && \  
rm -rf /var/cache/apk/*  
  
ARG GLIDE_VERSION  
ENV GLIDE_VERSION ${GLIDE_VERSION:-0.12.3}  
  
RUN go get github.com/Masterminds/glide && \  
cd "${GOPATH}/src/github.com/Masterminds/glide" && \  
git checkout "v${GLIDE_VERSION}" && \  
go install  
  
CMD ["glide", "install"]  


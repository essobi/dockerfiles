FROM golang:alpine3.6 AS binary  
ADD . /app  
WORKDIR /app  
RUN apk add \--no-cache git &&\  
go get "github.com/Tomasen/realip" &&\  
go build -o http  
  
FROM alpine:3.6  
WORKDIR /app  
ENV PORT 8000  
EXPOSE 8000  
COPY \--from=binary /app/http /app  
CMD ["/app/http"]  
  
ARG BUILD_DATE  
ARG BUILD_VCS_REF  
ARG BUILD_VERSION  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/mgvazquez/docker-whoami.git" \  
org.label-schema.vcs-ref=$BUILD_VCS_REF \  
org.label-schema.version=$BUILD_VERSION \  
com.microscaling.license=MIT


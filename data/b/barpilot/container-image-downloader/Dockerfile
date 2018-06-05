FROM golang:1.10-alpine AS build  
  
RUN adduser container-image-downloader -S -D -H -s /usr/sbin/nologin  
RUN apk add --update build-base gpgme-dev git  
RUN sed -i -e 's/v[[:digit:]]\\.[[:digit:]]/edge/g' /etc/apk/repositories &&
apk add --update dep  
COPY Gopkg.lock Gopkg.toml /go/src/github.com/barpilot/container-image-
downloader/  
WORKDIR /go/src/github.com/barpilot/container-image-downloader  
RUN dep ensure -v --vendor-only  
COPY . /go/src/github.com/barpilot/container-image-downloader  
RUN go build -a -o app  
  
FROM alpine  
RUN apk add --update gpgme ca-certificates  
COPY \--from=build /etc/passwd /etc/passwd  
USER container-image-downloader  
COPY \--from=build /go/src/github.com/barpilot/container-image-downloader/app
/container-image-downloader  
EXPOSE 8080  
ENTRYPOINT ["/container-image-downloader"]  


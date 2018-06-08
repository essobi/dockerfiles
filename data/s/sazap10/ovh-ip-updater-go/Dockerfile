FROM golang:1-alpine as builder  
  
# Add git for downloading dependencies  
RUN apk add --no-cache git  
  
WORKDIR /go/src/github.com/sazap10/ovh-ip-updater-go  
  
RUN go get -u github.com/golang/dep/cmd/dep  
  
COPY Gopkg.toml Gopkg.lock ./  
  
RUN dep ensure -vendor-only  
  
ADD main.go ./  
  
RUN go build  
  
###############################################################################  
  
FROM alpine:3.7  
  
ENV BUILD_DIR=/go/src/github.com/sazap10/ovh-ip-updater-go  
  
WORKDIR /app  
  
RUN apk add --no-cache ca-certificates  
  
COPY --from=builder $BUILD_DIR/ovh-ip-updater-go .  
  
CMD ["./ovh-ip-updater-go"]


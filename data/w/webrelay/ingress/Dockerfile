FROM golang:1.9.2  
# TODO(k): vendor  
# RUN go get github.com/golang/dep/cmd/dep  
# COPY Gopkg.toml Gopkg.lock ./  
# RUN dep ensure -v -vendor-only  
# COPY cmd cmd  
# COPY internal internal  
COPY . /go/src/github.com/rusenask/webrelay-ingress  
WORKDIR /go/src/github.com/rusenask/webrelay-ingress  
  
RUN CGO_ENABLED=0 GOOS=linux go install -ldflags="-w -s"
github.com/rusenask/webrelay-ingress/cmd/reingress  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
COPY \--from=0 /go/bin/reingress /bin/reingress  


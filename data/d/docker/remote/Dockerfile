FROM golang:1.8 AS build_env  
WORKDIR /go/src/github.com/fermayo/remote/  
ENV CGO_ENABLED 0  
ENV GOARCH amd64  
ENV GOOS=linux  
  
ADD . /go/src/github.com/fermayo/remote  
RUN GOOS=linux go build -v -o /remote-server ./cmd/remote-server  
  
FROM golang:1.8-alpine AS ngrok_build_env  
WORKDIR /ngrok  
RUN apk --no-cache add git build-base  
RUN git clone https://github.com/tutumcloud/ngrok.git /ngrok  
RUN make release-client  
  
FROM docker  
RUN apk --no-cache add ca-certificates  
ADD https://www.gandi.net/static/CAs/GandiStandardSSLCA2.pem /usr/share/ca-
certificates/gandi.crt  
RUN cat /usr/share/ca-certificates/gandi.crt >> /etc/ssl/certs/ca-
certificates.crt  
COPY \--from=ngrok_build_env /ngrok/bin/ngrok /usr/bin/ngrok  
COPY \--from=build_env /remote-server /remote-server  
  
CMD ["/remote-server", "run"]  


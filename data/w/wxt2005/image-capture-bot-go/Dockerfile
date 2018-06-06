FROM golang:1.10  
ENV ENV=prod  
  
RUN curl -fsSL -o /usr/local/bin/dep
https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 &&
chmod +x /usr/local/bin/dep  
  
RUN mkdir -p /go/src/github.com/wxt2005/image_capture_bot_go  
WORKDIR /go/src/github.com/wxt2005/image_capture_bot_go  
COPY . .  
  
RUN dep ensure -vendor-only  
RUN go build -o app .  
  
CMD ["./app"]  


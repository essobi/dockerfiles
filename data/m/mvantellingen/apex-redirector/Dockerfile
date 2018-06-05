# build stage  
FROM golang:1.9-alpine AS build-env  
RUN apk add --no-cache curl git  
  
RUN curl -fsSL -o /usr/local/bin/dep
https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64 &&
chmod +x /usr/local/bin/dep  
  
WORKDIR /go/src/labdigital.nl/apexredirector  
  
COPY Gopkg.toml Gopkg.lock ./  
  
RUN dep ensure -vendor-only  
  
COPY . ./  
  
RUN go build  
  
# final stage  
FROM alpine  
RUN adduser -S apexredirector  
  
USER apexredirector  
WORKDIR /app  
COPY \--from=build-env /go/src/labdigital.nl/apexredirector/apexredirector
/app/  
  
ENTRYPOINT ["./apexredirector"]  
  
EXPOSE 8080 8443  


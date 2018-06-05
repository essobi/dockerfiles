FROM golang:1.9-alpine AS build  
RUN apk --no-cache update && \  
apk --no-cache add make ca-certificates git && \  
rm -rf /var/cache/apk/*  
WORKDIR /go/src/github.com/sethpollack/bogie  
RUN go get -u github.com/golang/dep/cmd/dep  
COPY Gopkg.toml Gopkg.lock ./  
RUN dep ensure -v -vendor-only  
COPY . ./  
RUN CGO_ENABLED=0 GOOS=linux go build -installsuffix cgo -ldflags \  
"-X github.com/sethpollack/bogie/version.Version=`git describe --tags` -X
github.com/sethpollack/bogie/version.Commit=`git log -n 1
--pretty=format:"%h"`" \  
-o bin/bogie  
  
FROM scratch AS bogie  
LABEL maintainer="Seth Pollack <spollack@beenverified.com>"  
COPY \--from=build /etc/ssl/certs/ /etc/ssl/certs/  
COPY \--from=build /go/src/github.com/sethpollack/bogie/bin/bogie
/usr/local/bin/bogie  
ENTRYPOINT ["/usr/local/bin/bogie"]  
CMD ["--help"]  


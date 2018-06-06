FROM golang:1.6.3-alpine  
  
COPY . /go/src/uct  
  
ENV APP_PACKAGE="uct/scrapers/rutgers"  
ENV APP_NAME="rutgers"  
RUN apk --no-cache add ca-certificates openssl git && \  
update-ca-certificates && \  
wget
https://github.com/Masterminds/glide/releases/download/v0.12.1/glide-v0.12.1-linux-
amd64.tar.gz && \  
tar -xzf glide-v0.12.1-linux-amd64.tar.gz && \  
mv linux-amd64/glide /usr/bin && \  
cd /go/src/uct && \  
glide install && \  
rm -rf *.tar.gz* && \  
apk del git openssl  
  
RUN go install -v ${APP_PACKAGE}  
  
WORKDIR /go/src/uct  
EXPOSE 13301  
ENTRYPOINT ["rutgers", "--campus", "NK", "--daemon", "2m", "--latest", "-f" ,
"protobuf", "-c" , "/go/src/uct/common/conf/config.toml"]


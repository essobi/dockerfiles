From nimmis/alpine-glibc  
  
MAINTAINER nimmis <kjell.havneskold@gmail.com>  
  
RUN apk update && apk upgrade && \  
  
# Make info file about this build  
mkdir -p /etc/BUILDS/ && \  
printf "Build of nimmis/alpine-golang:1.7, date: %s\n" `date -u
+"%Y-%m-%dT%H:%M:%SZ"` > /etc/BUILDS/alpine-golang && \  
  
# add extra package for installation  
apk add curl && \  
  
# download and upack golang  
curl https://storage.googleapis.com/golang/go1.7.linux-amd64.tar.gz | tar xzf
- -C / && \  
mv /go /goroot && \  
  
# remove extra packages  
apk del curl && \  
  
# remove cached info  
rm -rf /var/cache/apk/*  
  
ENV GOROOT=/goroot \  
GOPATH=/gopath \  
GOBIN=/gopath/bin \  
PATH=${PATH}:/goroot/bin:/gopath/bin  


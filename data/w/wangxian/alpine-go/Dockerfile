FROM golang:1.10.3-alpine3.7  
# 0:clean offical golang setting  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN rm -rfv /go  
  
# 1:fix tzdata timezone alpine  
RUN apk add --no-cache curl tzdata && cp /usr/share/zoneinfo/PRC
/etc/localtime && echo "PRC" > /etc/timezone && apk del tzdata  
  
# 2:modify gopath  
ENV GOPATH /app  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin"  
WORKDIR $GOPATH  


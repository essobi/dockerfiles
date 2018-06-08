FROM muninn/glide:alpine AS build-env  
ADD . /go/src/app  
WORKDIR /go/src/app  
RUN glide install  
RUN GOOS=linux ARCH=amd64 go build -o /go/src/app/app-server  
  
FROM alpine:edge  
RUN apk add -U tzdata  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
RUN apk update && apk upgrade \  
&& apk add ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
COPY \--from=build-env /go/src/app/app-server /usr/local/bin/app-server  
EXPOSE 5050  
CMD ["app-server"]  


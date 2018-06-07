FROM alpine:latest  
RUN apk add --no-cache --update \  
&& apk add go ca-certificates libssh2 libcurl expat pcre git make git musl-dev  
  
RUN go get github.com/chinacoolhacker/headerget  
WORKDIR /root/go/src/github.com/chinacoolhacker/headerget/  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /root/headerget
.  
  
FROM alpine:latest  
#RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=0 /root/headerget /usr/bin/headerget  
CMD ["/usr/bin/headerget"]  


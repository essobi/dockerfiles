FROM strebul/go-builder1.9.2-alpine3.6 as builder  
WORKDIR /go/src/github.com/2at2/telegacli  
COPY . .  
RUN set -ex \  
&& make deps \  
&& make ok \  
&& make build  
  
FROM alpine:3.6  
COPY \--from=builder /go/src/github.com/2at2/telegacli/bin/telegacli
/usr/bin/telegacli  
RUN set -ex \  
&& apk add --no-cache ca-certificates \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*  
ENTRYPOINT ["telegacli"]  


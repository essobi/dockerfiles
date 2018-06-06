FROM alpine:latest  
  
  
# install requirements  
RUN apk update  
RUN apk add ca-certificates  
  
# install web server  
RUN apk add lighttpd  
  
# build app  
ENV GOPATH /go  
run apk add --no-cache --repository
https://dl-3.alpinelinux.org/alpine/edge/community go git gcc libc-dev libgcc  
RUN /usr/bin/go get github.com/sourcegraph/checkup/cmd/checkup  
RUN cp /go/bin/checkup /usr/bin/checkup  
RUN cp -r /go/src/github.com/sourcegraph/checkup/statuspage/*
/var/www/localhost/htdocs/  
RUN apk del --purge go git gcc libc-dev libgcc  
RUN rm -rf $GOPATH  
  
# add fs mode in html  
RUN sed -i '\|js/s3| s|$| <script src="js/fs.js"></script>|'
/var/www/localhost/htdocs/index.html  
  
# clean / optimise docker size  
RUN apk cache clean &  
RUN rm -rf /var/cache/apk/*  
RUN rm -rf /tmp/* /var/tmp/*  
  
# running  
EXPOSE 80  
ENV CHECK_INTERVALl ${PRELUDE_VERSION:-10m}  
ENTRYPOINT lighttpd -f /etc/lighttpd/lighttpd.conf && checkup every
$CHECK_INTERVALl  


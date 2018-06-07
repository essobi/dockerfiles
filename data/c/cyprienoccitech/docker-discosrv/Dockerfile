FROM golang:1.9 AS builder  
  
RUN git clone https://github.com/syncthing/syncthing
/go/src/github.com/syncthing/syncthing  
  
WORKDIR /go/src/github.com/syncthing/syncthing  
  
RUN git checkout tags/v0.14.45  
  
ENV CGO_ENABLED=0  
ENV BUILD_HOST=syncthing.net  
ENV BUILD_USER=docker  
RUN rm -f syncthing && go run build.go build stdiscosrv  
  
FROM alpine  
  
RUN apk add --no-cache ca-certificates  
  
COPY \--from=builder /go/src/github.com/syncthing/syncthing/stdiscosrv
/bin/stdiscosrv  
  
RUN echo 'syncthing:x:1000:1000::/var/syncthing:/sbin/nologin' >> /etc/passwd
\  
&& echo 'syncthing:!::0:::::' >> /etc/shadow \  
&& mkdir /var/syncthing \  
&& chown syncthing /var/syncthing  
  
WORKDIR /var/syncthing  
  
USER syncthing  
ENV STNOUPGRADE=1  
EXPOSE 8443  
HEALTHCHECK \--interval=1m --timeout=10s \  
CMD nc -z localhost 8443 || exit 1  
  
ENTRYPOINT ["/bin/stdiscosrv"]  


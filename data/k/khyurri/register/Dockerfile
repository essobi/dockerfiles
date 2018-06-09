FROM golang:1.10.2 as build  
  
RUN mkdir -p /go/src/github.com/khyurri/register  
WORKDIR /go/src/github.com/khyurri/register  
  
ADD main.go ./  
ADD server ./server  
ADD vendor ./vendor  
ADD client ./client  
  
RUN ls -la  
  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o register
main.go  
  
FROM alpine:latest  
  
WORKDIR /srv  
  
ADD start.sh /srv/start.sh  
RUN chmod +x /srv/start.sh  
  
RUN chown -R root:root /srv  
  
COPY \--from=build /go/src/github.com/khyurri/register/register /srv/  
CMD ["/srv/start.sh"]


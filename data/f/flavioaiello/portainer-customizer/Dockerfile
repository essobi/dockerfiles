### Source build ###  
FROM golang:1.9 as build  
  
COPY src /  
  
WORKDIR /build  
  
RUN go get -d -v -t;\  
CGO_ENABLED=0 GOOS=linux go build -v -o /usr/local/bin/serve  
  
### Runtime build ###  
FROM scratch  
# alpine:3.7  
#RUN set -ex;\  
# apk update;\  
# apk upgrade;\  
# apk add --no-cache curl;\  
# rm -rf /var/cache/apk/*  
COPY \--from=build /usr/local/bin/serve /usr/local/bin/  
  
COPY files /  
  
WORKDIR /wwwroot  
  
EXPOSE 8080  
#ENTRYPOINT ["entrypoint.sh"]  
CMD ["/usr/local/bin/serve", "-p", "8080", "-d", "/wwwroot"]  


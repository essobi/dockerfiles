FROM golang:1.7.6  
RUN grep "nobody" /etc/passwd > /tmp/passwd.stripped  
WORKDIR /go/src/  
COPY helloservice.go .  
RUN CGO_ENABLED=0 go build -a -installsuffix cgo -ldflags '-s' helloservice.go  
  
FROM scratch  
MAINTAINER mo@oclab.net  
COPY \--from=0 /go/src/helloservice /helloservice  
COPY \--from=0 /tmp/passwd.stripped /etc/passwd  
EXPOSE 8080  
USER nobody  
CMD [ "/helloservice" ]  


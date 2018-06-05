FROM golang:1.8-alpine  
  
COPY . /go/src/github.com/verath/owbot-bot  
RUN go install github.com/verath/owbot-bot  
  
VOLUME /db  
  
ENTRYPOINT ["owbot-bot", "-dbfile", "/db/owbot.boltdb"]  


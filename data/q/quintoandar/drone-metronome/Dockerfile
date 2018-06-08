FROM golang:1.9-alpine  
WORKDIR /go/src/github.com/quintoandar/drone-metronome  
ADD . .  
RUN GOOS=linux CGO_ENABLED=0 go build -o /bin/drone-metronome \  
github.com/quintoandar/drone-metronome  
  
FROM scratch  
COPY \--from=0 /bin/drone-metronome /bin/drone-metronome  
ENTRYPOINT ["/bin/drone-metronome"]  


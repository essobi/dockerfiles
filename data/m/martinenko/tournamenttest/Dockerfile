FROM golang  
  
ADD . /go/src/github.com/Ch1f/tournamentTest  
  
RUN go get ./...  
  
RUN go install github.com/Ch1f/tournamentTest  
  
ENTRYPOINT /go/bin/tournamentTest  
  
EXPOSE 4000


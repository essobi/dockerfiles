FROM golang:latest  
  
ADD . /go/src/github.com/Pigmice2733/scouting-backend/  
WORKDIR /go/src/github.com/Pigmice2733/scouting-backend/  
  
RUN go get -t -v ./...  
  
WORKDIR /go/src/github.com/Pigmice2733/scouting-backend/cmd/scouting-backend  
  
RUN go install  
  
ENTRYPOINT [ "scouting-backend" ]


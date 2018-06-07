FROM golang:latest  
  
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh  
  
WORKDIR $GOPATH/src/bitbucket.org/andrey_kibenko/ht_backend  
  
COPY . .  
  
RUN dep ensure && GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o binary  
  
FROM debian  
  
RUN apt-get update -y && apt-get install ffmpeg -y  
  
WORKDIR /data/backend/  
  
COPY \--from=0 /go/src/bitbucket.org/andrey_kibenko/ht_backend/binary
/data/backend/  
  
EXPOSE 9999  
ENTRYPOINT /data/backend/binary


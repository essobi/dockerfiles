FROM golang:1.9.2  
COPY . /go/src/cc-project  
WORKDIR /go/src/cc-project  
  
RUN go get -v .  
CMD [ "go", "run", "main.go" ]  


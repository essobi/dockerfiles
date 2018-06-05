FROM golang:1.8  
ADD . /go/src/app  
WORKDIR /go/src/server  
COPY . .  
  
RUN go get -d -v ./...  
RUN go install -v ./...  
EXPOSE 3000 8080  
CMD ["server"]


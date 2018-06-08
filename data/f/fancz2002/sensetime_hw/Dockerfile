FROM golang:1.8  
WORKDIR /go/src/app  
COPY . .  
  
ENV GOROOT /usr/local/go  
ENV GOPATH /go/src/app  
CMD ["go", "run", "src/main.go"]  
  
#EXPOSE 21  
#EXPOSE 10000-11000  
#RUN go get -d -v ./...  
#Run go install -v ./...  


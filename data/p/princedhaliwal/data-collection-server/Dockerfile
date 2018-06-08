FROM golang:1.9.2  
WORKDIR /go/src/app  
COPY . .  
RUN go get -d -v .  
RUN go install -v .  
CMD [ "app" ]  


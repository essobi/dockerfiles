FROM golang:1.10  
WORKDIR /go/src/app  
COPY . /go/src/app  
  
RUN go get -d -v ./...  
RUN go install -v .  
  
RUN < /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};echo;>salt  
RUN mkdir -p uploads waifus  
RUN /go/src/app/scrapewaifus.sh  
  
EXPOSE 5000  
CMD ["app"]  


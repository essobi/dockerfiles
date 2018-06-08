FROM golang:latest  
  
RUN mkdir -p /go/src/github.com/gophergala/go_report  
WORKDIR /go/src/github.com/gophergala/go_report  
ENV PATH /go/bin:$PATH  
COPY . /go/src/github.com/gophergala/go_report  
  
# Dependencies  
RUN go get golang.org/x/tools/cmd/goimports  
RUN go get github.com/fzipp/gocyclo  
RUN go get github.com/golang/lint/golint  
RUN go get golang.org/x/tools/cmd/vet  
RUN go get labix.org/v2/mgo  
  
#RUN go-wrapper install  
#CMD ["go-wrapper", "run"]  
EXPOSE 8080  


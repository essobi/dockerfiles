FROM golang:onbuild  
RUN go get github.com/PuerkitoBio/goquery  
RUN go get github.com/otiai10/cachely  
RUN go get github.com/djimenez/iconv-go  
  
ADD main.go /go/src/app  
  
CMD ["go", "run", "main.go"]  
  
EXPOSE 8080  


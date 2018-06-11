FROM golang:1-alpine  
  
COPY *.go src/github.com/vadd/verbum-cli/  
RUN go install github.com/vadd/verbum-cli  
  
CMD ["verbum-cli"]  


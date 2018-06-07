FROM golang:1.8.3-alpine  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh curl  
  
RUN curl -s https://glide.sh/get | sh  
  
COPY ./glide.yaml /go/src/glide.yaml  
  
RUN cd /go/src/ && glide install  
  
RUN go install vendor/github.com/kubernetes-incubator/external-dns  
  
CMD ["external-dns"]  


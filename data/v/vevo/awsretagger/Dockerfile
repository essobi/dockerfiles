FROM golang:alpine  
  
RUN apk update \  
&& apk add --no-cache git \  
&& go get github.com/Masterminds/glide \  
&& go install github.com/Masterminds/glide  
  
WORKDIR /go/src/github.com/VEVO/awsRetagger  
COPY . ./  
  
RUN rm -f glide.lock \  
&& glide install --strip-vendor  
RUN go-wrapper install  
  
CMD ["go-wrapper", "run"]  


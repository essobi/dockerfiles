FROM golang:1.8-alpine3.6  
RUN apk add --no-cache git curl  
  
RUN mkdir -p /go/src/app  
  
# Get glide  
RUN curl https://glide.sh/get | sh  
  
WORKDIR /go/src/app  
  
ONBUILD COPY . /go/src/app  
  
ONBUILD RUN if [ -f glide.lock ] ; then echo "Install packages and
dependecies" && glide install ; else echo "No glide. Try to get dependecies
with get" && go-wrapper download ; fi && exit  
  
ONBUILD RUN go test ./...  
  
ONBUILD RUN go-wrapper install  
  
CMD ["/go/bin/app"]  


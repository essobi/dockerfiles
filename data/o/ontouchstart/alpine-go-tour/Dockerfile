FROM ontouchstart/alpine-go  
RUN apk add --update git  
RUN go version  
ENV GOPATH /home/  
ENV CGO_ENABLED 0  
RUN go get golang.org/x/tour/gotour  
ENTRYPOINT ["/home/bin/gotour"]  
  


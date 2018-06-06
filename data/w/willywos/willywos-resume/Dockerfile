FROM golang:alpine  
  
RUN apk add --update git  
  
WORKDIR /go/src/willywos-resume  
  
ADD . /go/src/willywos-resume  
  
# These are so it compiles with ARM and  
# work on the raspberry pi  
# remove them if you don't want to build it  
# for the pi.  
ENV GOOS linux  
ENV GOARCH arm  
ENV GOARM=7  
RUN go get -d -v  
RUN go install -v  
RUN go build .  
  
ENTRYPOINT willywos-resume  
  
EXPOSE 1982


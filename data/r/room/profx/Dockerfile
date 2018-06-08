FROM golang:1.5.1  
  
MAINTAINER Harrison Shoebridge <harrison@theshoebridges.com>  
  
RUN go get github.com/bigroom/vision/tunnel  
RUN go get github.com/nickvanw/ircx  
RUN go get github.com/paked/configure  
RUN go get github.com/sorcix/irc  
  
RUN go get github.com/codegangsta/gin  
  
RUN go get github.com/bigroom/profx  
  
RUN go get github.com/getsentry/raven-go  
RUN go get github.com/sirupsen/logrus  
RUN go get github.com/evalphobia/logrus_sentry  
RUN go get github.com/bigroom/vision/models  
  
# ADD . /go/src/github.com/bigroom/roomer for deployment...  
  
WORKDIR /go/src/github.com/bigroom/profx  
  
CMD gin -i -b "profx"  
#CMD go build && ./roomer  


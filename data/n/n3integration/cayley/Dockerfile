FROM golang:1.7.3-alpine  
MAINTAINER n3integration@gmail.com  
  
VOLUME /data  
EXPOSE 64210  
RUN apk add git curl --update --no-cache && \  
curl -s https://glide.sh/get | sh && \  
go get -d -v github.com/cayleygraph/cayley && \  
cd /go/src/github.com/cayleygraph/cayley && \  
glide install && \  
glide get github.com/linkeddata/gojsonld && \  
go install -v github.com/cayleygraph/cayley/cmd/cayley && \  
mkdir -p /etc/cayley && \  
mkdir -p /usr/local/cayley && \  
mv /go/bin/cayley /usr/local/cayley/bin && \  
mv docs /usr/local/cayley && \  
mv static /usr/local/cayley && \  
mv templates /usr/local/cayley && \  
rm -rf /var/cache/apk && \  
rm -rf /usr/share/man && \  
rm -rf /go  
  
ADD cayley.cfg /etc/cayley/cayley.cfg  
ADD cayley.sh /usr/local/bin/cayley  
  
ENTRYPOINT ["/usr/local/bin/cayley"]  


FROM alpine:3.2  
MAINTAINER Jonathan Gautheron <jgautheron@neverblend.in>  
  
ENV GOPATH /root/go  
ENV PATH $GOPATH/bin:$PATH  
  
RUN sed -i -e 's/v3\\.2/edge/g' /etc/apk/repositories  
RUN apk --update add go git bash && \  
rm -fR /var/cache/apk/*  
  
# create the GOPATH  
RUN mkdir /root/go  
  
ADD entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
# install gometalinter  
RUN go get github.com/alecthomas/gometalinter && \  
gometalinter --install --update  
  
# preloading dependencies  
RUN go get github.com/Sirupsen/logrus && \  
go get github.com/codegangsta/cli && \  
go get github.com/smartystreets/goconvey/convey  
  
WORKDIR /root/go  
ENTRYPOINT ["/entrypoint.sh"]


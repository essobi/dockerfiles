FROM golang:1.9-alpine3.7  
# Install Go, WebPageReplay and the webpagereplay wrapper  
#WORKDIR /work  
RUN apk --no-cache add \  
# libnss3-tools \  
openntpd \  
# curl \  
git \  
mc \  
vim \  
bash  
  
# build-essential \  
# iproute2 -y && \  
# mkdir -p $HOME/.pki/nssdb && \  
# certutil -d $HOME/.pki/nssdb -N  
# curl -O https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz && \  
# tar -xvf go1.9.linux-amd64.tar.gz && \  
# mv go /usr/local  
#ENV PATH="/usr/local/go/bin:${PATH}"  
RUN go get github.com/urfave/cli && \  
go get golang.org/x/net/http2 && \  
go get github.com/catapult-
project/catapult/web_page_replay_go/src/webpagereplay  
  
#WORKDIR /go/src/github.com/catapult-project/catapult/web_page_replay_go  
#RUN go run src/wpr.go installroot  
RUN mkdir -p /results  
  
#WORKDIR /go/src/github.com/catapult-project/catapult/web_page_replay_go  
VOLUME /results  
  
EXPOSE 8080  
EXPOSE 8081  
COPY start.sh start.sh  
COPY stop.sh stop.sh  
COPY test.sh test.sh  
  
RUN chmod +x start.sh  
RUN chmod +x stop.sh  
RUN chmod +x test.sh  
  
ENTRYPOINT ["./start.sh"]  
  
#CMD ["/usr/sbin/ntpd", "-d"]


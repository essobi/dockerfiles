FROM golang:latest  
  
RUN apt-get update && apt-get clean  
RUN apt-get install jq -y && apt-get clean  
  
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh  
  
RUN wget -O release.tar.gz $(curl https://api.github.com/repos/shazow/ssh-
chat/releases | jq .[0].zipball_url | sed -e s/\"//g -e s/zipball/tarball/g)  
  
RUN tar xvfz release.tar.gz && \  
mv shazow-ssh-chat-* /go/src/ssh-chat  
  
RUN cd /go/src/ssh-chat/ && \  
export GOPATH=/go && \  
make && \  
go build ./cmd/ssh-chat/  
  
FROM debian:latest  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
COPY \--from=0 /go/src/ssh-chat/ssh-chat /ssh-chat  
  
ENTRYPOINT ["/entrypoint.sh"]  


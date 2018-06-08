FROM node:latest  
ENV GOPATH /go  
ENV PATH "${PATH}:${GOPATH}/bin"  
  
RUN mkdir /go /go/src /go/pkg /go/bin && \  
apt-get update && \  
apt-get -y install golang && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
go get github.com/andygarfield/worshipup  
  
WORKDIR /go/src/github.com/andygarfield/worshipup  
RUN yarn && \  
yarn run prod  
  
ENTRYPOINT ["worshipup"]


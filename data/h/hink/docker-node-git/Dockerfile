FROM circleci/golang:latest  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
RUN sudo apt-get update && sudo apt-get install -y nodejs \  
ca-certificates \  
yarn \  
make \  
python \  
unzip \  
openrc \  
openssh-client  
  
VOLUME ["/var/run/docker.sock"]  
RUN sudo npm install --unsafe-perm --global --production resin-cli@6.13 raven  
RUN go get -u github.com/golang/dep/cmd/dep \  
github.com/golang/mock/gomock \  
github.com/golang/mock/mockgen\  
github.com/kisielk/errcheck  
  
# Protobuf  
ENV PROTOBUF_VERSION 3.5.1  
WORKDIR /tmp  
RUN curl -fsSL
https://github.com/google/protobuf/releases/download/v$PROTOBUF_VERSION/protoc-$PROTOBUF_VERSION-
linux-x86_64.zip -o protobuf.zip  
RUN unzip protobuf.zip -d protoc3  
RUN sudo mv protoc3/bin/* /usr/local/bin/  
RUN sudo mv protoc3/include/* /usr/local/include/  
  
RUN sudo rm -r /tmp/*  
RUN go get -u github.com/golang/protobuf/protoc-gen-go  
  
CMD ["sh"]  


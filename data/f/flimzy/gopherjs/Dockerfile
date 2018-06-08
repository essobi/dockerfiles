FROM golang:1.10-stretch  
  
ENV NODE_PATH=/usr/lib/node_modules  
# Install Node.js related dependencies  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install --global node-gyp source-map-support  
  
# Install GopherJS  
RUN go get -u github.com/gopherjs/gopherjs  
# Add syscall support  
RUN ( cd $GOPATH/src/github.com/gopherjs/gopherjs/node-syscall && node-gyp
rebuild && mkdir -p ~/.node_libraries/ && cp build/Release/syscall.node
~/.node_libraries/syscall.node )  


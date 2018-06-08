FROM golang  
MAINTAINER miles.dev@outlook.com firemiles  
  
RUN go get -u -d github.com/7sDream/rikka && \  
cd $GOPATH/src/github.com/7sDream/rikka && \  
mkdir -p /www/rikka/ && \  
go build ./ && \  
mv $GOPATH/src/github.com/7sDream/rikka/rikka /www/rikka/ && \  
mv $GOPATH/src/github.com/7sDream/rikka/server /www/rikka/server && \  
rm -rf $GOPATH/src/*  
  
WORKDIR /www/rikka  
  
ENTRYPOINT ["./rikka"]  


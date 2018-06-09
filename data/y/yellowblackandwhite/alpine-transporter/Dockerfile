FROM yellowblackandwhite/alpine-golang  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
  
ENV CONFIG '/app/config.yaml'  
ENV APP '/app/application.js'  
WORKDIR /rest  
ADD ./rest.go /rest/main.go  
  
# RUN /bin/bash go-wrapper download github.com/compose/transporter/...  
# RUN /bin/bash go-wrapper install github.com/compose/transporter/...  
RUN mkdir -p $GOPATH/src/github.com/compose && \  
apk --update add gcc build-base && \  
go get github.com/tools/godep && \  
go get github.com/ant0ine/go-json-rest/rest && \  
cd $GOPATH/src/github.com/compose && git clone
https://github.com/Alino/transporter.git && \  
cd transporter && git checkout patch-1 && \  
cd $GOPATH/src/github.com/compose/transporter && \  
go get -a ./cmd/... && go build -a ./cmd/...  
RUN go build -o main . && \  
apk del build-base gcc && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
EXPOSE 8080  
USER alpine  
WORKDIR /app  
VOLUME ["/app"]  
CMD ["/rest/main"]  


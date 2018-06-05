FROM golang:1.7  
RUN go get -u github.com/kardianos/govendor && \  
go get -d github.com/aandryashin/selenoid && \  
cd $GOPATH/src/github.com/aandryashin/selenoid && govendor sync && go build &&
\  
cp $GOPATH/src/github.com/aandryashin/selenoid/selenoid /usr/bin/selenoid  
  
ADD etc/selenoid /etc/selenoid  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENV DOCKER_API='unix:///var/run/docker.sock'  
ENV MAX_INSTANCES=5  
VOLUME /etc/selenoid  
  
EXPOSE 4444  
ENTRYPOINT /entrypoint.sh


FROM golang  
MAINTAINER Frederic Branczyk <fbranczyk@gmail.com>  
  
RUN go get github.com/constabulary/gb/...  
  
RUN mkdir -p /go/src/github.com/emerald-ci/webhook-plugin  
COPY . /go/src/github.com/emerald-ci/webhook-plugin  
RUN cd /go/src/github.com/emerald-ci/webhook-plugin && make  
RUN mv /go/src/github.com/emerald-ci/webhook-plugin/bin/webhookplugin
/bin/webhookplugin && chmod +x /bin/webhookplugin  
  
WORKDIR /project  
ENTRYPOINT ["/bin/webhookplugin"]  
  


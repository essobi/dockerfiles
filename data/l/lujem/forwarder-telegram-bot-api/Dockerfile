FROM golang  
  
ENV app forwarder-telegram-bot-api  
ENV root /go/src/github.com/lujem/${app}  
ENV entry /go/bin/${app}  
  
ADD . ${root}  
  
WORKDIR ${root}  
  
RUN make install ENV=production  
  
ENTRYPOINT ["/go/bin/forwarder-telegram-bot-api"]  


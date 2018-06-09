FROM golang  
  
ENV app stranger-telgram-bot-api  
ENV root /go/src/github.com/lujem/${app}  
  
ADD . ${root}  
  
WORKDIR ${root}  
  
RUN make install  
  
ENTRYPOINT [ "/go/bin/stranger-telgram-bot-api" ] # fixme: use env  


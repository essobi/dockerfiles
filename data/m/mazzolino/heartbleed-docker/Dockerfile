FROM miksago/ubuntu-go  
  
RUN go get github.com/FiloSottile/Heartbleed  
RUN go install github.com/FiloSottile/Heartbleed  
  
ENTRYPOINT ["Heartbleed"]  


FROM google/golang  
  
RUN go get github.com/doug/turnhttp/turnhttp-server  
RUN go get github.com/doug/turnhttp/turnhttp-secret  
  
CMD -port 8080 -secret notasecret -servers localhost -domains
http://localhost:8080  


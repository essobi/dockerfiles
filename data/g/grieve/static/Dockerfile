FROM golang  
MAINTAINER Ryan Grieve<me@ryangrieve.com>  
  
ADD serve.go /serve.go  
RUN cd / && go build serve.go  
  
VOLUME ["/static"]  
  
EXPOSE 3000  
WORKDIR /  
CMD ./serve  


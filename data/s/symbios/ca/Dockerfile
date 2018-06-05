FROM golang  
MAINTAINER Dario Nascimento <dfrnascimento@gmail.com>  
COPY start.sh /start.sh  
RUN go get -u github.com/dnascimento/symbios/src/symbios  
RUN go get github.com/dgrijalva/jwt-go  
RUN go install github.com/dnascimento/symbios/src/symbios  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  
  


FROM golang  
MAINTAINER tech@texastribune.org  
  
RUN go get github.com/bitly/google_auth_proxy  
  
EXPOSE 4180  
ENTRYPOINT ["google_auth_proxy"]  


FROM golang:1.5  
  
RUN apt-get update && apt-get install -q -y libltdl-dev  
  
RUN go get -u github.com/thesamet/cfssl/cmd/cfssl  
  
RUN go get -u github.com/thesamet/cfssl/cmd/...  
  
ENTRYPOINT ["cfssl"]  
  


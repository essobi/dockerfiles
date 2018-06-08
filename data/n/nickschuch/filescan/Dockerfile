FROM golang:1.4  
Add . /opt/filescan  
WORKDIR /opt/filescan  
  
# Get the libraries.  
RUN go get github.com/dutchcoders/go-clamd  
RUN go get gopkg.in/alecthomas/kingpin.v1  
  
# Build the binary.  
RUN go build  
  
EXPOSE 80  
ENTRYPOINT ["./filescan"]  


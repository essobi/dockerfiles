FROM golang:latest  
  
# Store application in /app  
RUN mkdir /app  
ADD . /app/  
WORKDIR /app  
  
# Install system dependenceis  
RUN apt-get update && apt-get install -y libpcap-dev  
  
# Grab Go deps and install  
RUN go get github.com/google/gopacket/pcap  
RUN go get github.com/unrolled/render  
RUN go build -o main .  
  
EXPOSE 80  
CMD ["/app/main"]  


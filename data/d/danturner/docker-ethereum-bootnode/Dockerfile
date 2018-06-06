FROM ubuntu:trusty  
  
RUN apt-get update  
RUN apt-get install -y wget  
RUN wget https://s3-ap-southeast-2.amazonaws.com/go-
ethereum/master/latest/bootnode-linux-amd64  
RUN chmod +x bootnode-linux-amd64  
RUN mv bootnode-linux-amd64 /usr/bin/bootnode  
  
EXPOSE 30303  
EXPOSE 30301/udp  
  
ENTRYPOINT ["/usr/bin/bootnode"]  


FROM ubuntu:latest  
RUN apt-get -y update && apt-get install -y mumble-server; apt-get clean  
ADD mumble-server.ini /etc/mumble-server.ini  
CMD murmurd -v -fg -ini /etc/mumble-server.ini  


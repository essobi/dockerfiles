FROM ubuntu:xenial  
MAINTAINER dbarroso@fastly.com  
  
LABEL fastly.net101.name=base  
  
WORKDIR /root  
  
RUN apt-get update; apt-get upgrade -y;  
RUN apt-get install -y ucf iproute mtr-tiny traceroute iputils-ping less
tcpdump net-tools curl dnsutils  
  
COPY ./run.sh /bin/run.sh  
  
ENTRYPOINT ["/bin/run.sh"]  


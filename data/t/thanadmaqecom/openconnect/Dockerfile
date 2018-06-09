FROM ubuntu:16.04  
RUN apt-get update &&\  
apt-get install -y \  
curl git vim openconnect openssh-client inetutils-traceroute netcat-
traditional dnsutils telnet &&\  
apt-get clean &&\  
rm -rf /var/cache/apt/* &&\  
rm -rf /var/lib/apt/lists/*  
  
ADD connect.sh /root  
  
RUN chmod +x /root/connect.sh  
  
CMD ["/root/connect.sh"]  


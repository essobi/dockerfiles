# shadowsocks-net-speeder  
FROM itscaro/debian-ssh:latest  
#MAINTAINER itscaro <lowid@outlook.com>  
RUN apt-get update && \  
apt-get install -y python-pip libnet1 libnet1-dev libpcap0.8 libpcap0.8-dev
git  
  
RUN pip install shadowsocks==2.8.2  
  
  
# Configure container to run as an executable  
ENTRYPOINT ["/usr/bin/ssserver"]  


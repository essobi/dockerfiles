# shadowsocks-net-speeder  
FROM ubuntu:14.04.3  
MAINTAINER lowid <lowid@outlook.com>  
RUN apt-get update && \  
apt-get install -y python-pip libnet1 libnet1-dev libpcap0.8 libpcap0.8-dev
git  
  
RUN pip install shadowsocks==2.8.2  
  
RUN git clone https://github.com/snooda/net-speeder.git net-speeder  
WORKDIR net-speeder  
RUN sh build.sh  
  
RUN mv net_speeder /usr/local/bin/  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/net_speeder  
  
# Configure container to run as an executable  
EXPOSE 1080  
#CMD ssserver -p 80 -m aes-256-cfb -k 888888  
ENTRYPOINT /usr/local/bin/ssserver -p 1080 -m aes-256-cfb -k 888888  


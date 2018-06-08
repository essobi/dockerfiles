FROM ubuntu:rolling  
  
RUN apt update &&\  
apt-get install -y shadowsocks &&\  
echo "net.core.default_qdisc=fq" >> /etc/sysctl.d/99-sysctl.conf &&\  
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.d/99-sysctl.conf  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  


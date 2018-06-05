FROM debian:jessie  
RUN apt-get update && \  
apt-get install --no-install-recommends -y curl vim nmap traceroute
tcptraceroute strace dnsutils socat netcat mtr-tiny iperf tcpdump telnet
openssl && \  
apt-get clean -y && \  
apt-get autoclean -y && \  
apt-get autoremove -y  
ENTRYPOINT ["tail", "-f", "/dev/null"]  


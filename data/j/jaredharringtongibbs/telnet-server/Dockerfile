FROM ubuntu:17.10  
LABEL maintainer="Jared Harrington-Gibbs"  
LABEL description="A docker running a completely insecure telnet server"  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install telnetd xinetd && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
rm -rf /var/lib/apt/lists/* && \  
echo root:malware | chpasswd && \  
echo "# default: on \n \  
# description: The telnet server serves telnet sessions; it uses unencrypted
username/password pairs for authentication. \n \  
service telnet \n \  
{ \n \  
disable = no \n \  
flags = REUSE \n \  
socket_type = stream \n \  
wait = no \n \  
user = root \n \  
server = /usr/sbin/in.telnetd \n \  
log_on_failure += USERID \n \  
}" | tee -a /etc/xinetd.d/telnet && \  
rm -f /etc/securetty  
  
ENTRYPOINT ["bash"]  
CMD ["-c","xinetd -dontfork -stayalive"]  


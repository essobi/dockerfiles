FROM ubuntu  
MAINTAINER Giorgio Regni <gr@scalilty.com>  
  
RUN apt-get update  
RUN apt-get install -y iperf iftop tcpdump bmon sysstat telnet vim wget curl
strace netcat mtr  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY . /root/scripts  
  
CMD [ "iperf", "-s" ]  
EXPOSE 5001  


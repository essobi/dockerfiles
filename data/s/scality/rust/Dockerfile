FROM ubuntu  
MAINTAINER Giorgio Regni <gr@scalilty.com>  
  
# Some developement tools you may want to have at your disposal  
RUN apt-get update  
RUN apt-get install -y iperf iftop tcpdump bmon sysstat telnet vim wget curl
strace netcat sudo  
RUN apt-get install -y build-essential  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install Rust, taken from https://www.rust-lang.org/en-US/downloads.html  
RUN curl -sSf https://static.rust-lang.org/rustup.sh | sh  
  
RUN mkdir /app  
RUN cd /app  
  
CMD [ "bash", "--login" ]  
EXPOSE 80  


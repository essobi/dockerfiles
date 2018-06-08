FROM ubuntu:latest  
MAINTAINER = jack liu <jackl3@cisco.com>  
RUN apt-get update  
RUN apt-get install -y build-essential  
  
ADD https://github.com/SIPp/sipp/archive/v3.4.1.tar.gz /  
RUN tar -xzf /v3.4.1.tar.gz  
  
RUN apt-get install -y libssl-dev libpcap-dev libsctp-dev libncurses5-dev  
  
WORKDIR /sipp-3.4.1  
RUN ./configure --with-pcap --with-sctp --with-openssl --with-rtpstream  
RUN make install  
  
WORKDIR /  
RUN mkdir /scens  
RUN mkdir /logs  
RUN rm -rf v3.4.1.tar*  
RUN rm -rf sipp-3.4.1  
  
VOLUME /scens  
VOLUME /logs  
  
EXPOSE 5060-5070  
CMD ["/usr/bin/tail", "-f", "/dev/null"]  


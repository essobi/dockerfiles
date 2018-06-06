FROM ruby:2.4.3-jessie  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
build-essential \  
libncurses5-dev \  
libpcap-dev \  
libsctp-dev \  
libssl-dev \  
python \  
python-pip \  
vim  
  
WORKDIR /  
  
ADD https://github.com/SIPp/sipp/releases/download/v3.5.1/sipp-3.5.1.tar.gz /  
RUN tar -zxvf sipp-3.5.1.tar.gz  
  
WORKDIR /sipp-3.5.1  
RUN ls -l && ./configure --with-pcap --with-sctp --with-openssl --with-
rtpstream && make install  
RUN gem install packetfu:1.1.11  
RUN git clone https://github.com/mojolingo/sippy_cup.git && cd sippy_cup &&
bundle install  
  
WORKDIR /  
RUN rm -rf v3.4.1.tar sipp-3.4.1  


FROM ubuntu:15.10  
MAINTAINER Shunsuke Otani <shun.otani@gmail.com>  
  
RUN apt-get install -y wget liblzo2-2 liblzma5 liblua5.1-0  
  
RUN cd /root/ && wget
http://cdimage.debian.org/ubuntu/ubuntu/pool/universe/k/kyotocabinet/libkyotocabinet16_1.2.76-4_amd64.deb  
RUN dpkg --force-depends -i /root/libkyotocabinet16_1.2.76-4_amd64.deb  
  
RUN cd /root/ && wget
http://cdimage.debian.org/ubuntu/ubuntu/pool/universe/k/kyototycoon/libkyototycoon2_0.9.56-1_amd64.deb  
RUN dpkg -i /root/libkyototycoon2_0.9.56-1_amd64.deb  
  
RUN cd /root/ && wget
http://cdimage.debian.org/ubuntu/ubuntu/pool/universe/k/kyototycoon/kyototycoon_0.9.56-1_amd64.deb  
RUN dpkg -i /root/kyototycoon_0.9.56-1_amd64.deb  
  
EXPOSE 1978  
ENTRYPOINT ["ktserver"]  


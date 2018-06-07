FROM ubuntu:14.04.3  
RUN apt-get update && \  
apt-get install -y python-pip libnet1 libnet1-dev libpcap0.8 libpcap0.8-dev
git  
  
RUN apt-get install -y m2crypto  
  
RUN git clone https://github.com/Matrix42/ss-manyuser.git; \  
  
mv ss-manyuser /usr/local/bin/  
  
RUN git clone https://github.com/snooda/net-speeder.git net-speeder  
  
WORKDIR net-speeder  
  
RUN sh build.sh  
  
RUN mv net_speeder /usr/local/bin/  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/net_speeder  
  
EXPOSE 3306 8388  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  


FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -y socat && \  
rm -rf /var/lib/apt/lists/*  
  
ADD /logmein-hamachi-2.1.0.139-x64 /logmein-hamachi-2.1.0.139-x64  
ADD /bootstrap.sh /bootstrap.sh  
EXPOSE 80  
EXPOSE 443  
EXPOSE 22  
ENV LOACL_HOST TCP-LISTEN:80,fork  
ENV REMOTE_HOST TCP:0.0.0.0:80  
ENV HAMACHI_NET_ACC ""  
ENV HAMACHI_NET_PASS ""  
ENTRYPOINT ["/bootstrap.sh"]  


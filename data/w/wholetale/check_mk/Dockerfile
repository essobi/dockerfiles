FROM debian:jessie  
  
RUN apt-get update -y && apt-get install bash curl python3 python3-pip xinetd
-y && \  
pip3 install docker  
  
COPY check_mk/etc /etc/  
COPY check_mk/usr /usr/  
COPY scripts/ /scripts  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT "/entrypoint.sh"  


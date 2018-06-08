FROM ubuntu:14.04  
ADD ./frps /frp/frps  
ADD ./frps.ini /frp/frps.ini  
  
EXPOSE 7000  
EXPOSE 10000  
CMD ["/frp/frps","-c","/frp/frps.ini"]  


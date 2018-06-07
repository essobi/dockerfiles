FROM greatfox/ssh  
  
RUN apt-get -y install openvpn  
  
RUN echo 'service openvpn start' >> /initrc  
  
EXPOSE 1194/udp  


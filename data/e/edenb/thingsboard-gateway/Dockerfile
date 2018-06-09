FROM openjdk:8-jre  
RUN wget https://github.com/thingsboard/thingsboard-
gateway/releases/download/v1.4.0.1/tb-gateway-1.4.0.deb &&\  
dpkg -i tb-gateway-1.4.0.deb  
CMD ["/etc/init.d/tb-gateway","run"]  


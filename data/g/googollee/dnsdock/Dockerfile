FROM alpine  
EXPOSE 80  
EXPOSE 53/udp  
CMD ["/start.sh"]  
ADD start.sh /start.sh  
ADD
https://github.com/aacebedo/dnsdock/releases/download/v1.16.4/dnsdock.amd64
/dnsdock  
RUN chmod +x /dnsdock  


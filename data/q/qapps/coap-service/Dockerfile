# Version: 0.0.1  
FROM alpine  
  
MAINTAINER Yury Kavaliou <yury_kavaliou@epam.com>  
  
COPY ./observer /home/observer  
RUN chmod +x /home/observer  
  
ENTRYPOINT ["/home/observer"]  
CMD [""]  
  
EXPOSE 4000 56083/udp  


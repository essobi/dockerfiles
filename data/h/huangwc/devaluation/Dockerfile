FROM huangwc/django:latest  
MAINTAINER huangwc@easecloud.cn  
  
WORKDIR /var/app  
  
ADD ./* ./  
  
VOLUME ["/var/app"]  
  
RUN chmod +x build.sh && ./build.sh  
RUN chmod +x cmd.sh  
  
CMD ["./cmd.sh"]  
  


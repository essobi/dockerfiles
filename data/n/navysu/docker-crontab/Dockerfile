FROM alpine  
  
MAINTAINER Haijun (Navy) Su <navysu@gmail.com>  
  
RUN mkdir -p /jobs  
WORKDIR /jobs  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  


FROM nginx  
MAINTAINER Ioannis Angelakopoulos <ioagel@gmail.com>  
  
# Override the env values  
ENV USERNAME username  
ENV PASSWORD password  
ENV COMMON_NAME localhost  
ENV COUNTRY GR  
ENV STATE Attica  
ENV CITY Athens  
ENV ORGANIZATION FlouLab  
  
# Disable default standard http 80 unathenticated configuration  
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.inactive  
  
COPY ssl.conf /etc/nginx/conf.d/ssl.conf  
  
COPY start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
  
CMD ["start.sh"]  


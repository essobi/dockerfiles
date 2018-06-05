FROM chagridsada/cacti  
MAINTAINER The-Dollarsigns <developer@the-dollarsign.com>  
  
## --- env ---  
ENV TZ Asia/Bangkok  
  
## --- timezone ---  
RUN echo "$TZ" > /etc/timezone  
RUN ln -sf /usr/share/zoneinfo/Asia/Bangkok /etc/localtime  
RUN echo "date.timezone = $TZ" >> /etc/php.ini  
  
## --- env ---  
ENV DB_USER=cacti DB_PASS=passwd DB_ADDRESS=127.0.0.1  
  
## --- system ---  
COPY resource /  
  
EXPOSE 80  
  
## EOF


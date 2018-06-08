FROM dockerfile/ubuntu  
MAINTAINER mibsen "m-ibsen@hotmail.com"  
RUN apt-get update  
RUN apt-get -qq install supervisor  
RUN rm -rf /var/lib/apt/lists/*  
  
ADD supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
  
EXPOSE 9001  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  


FROM java:8  
MAINTAINER Denys Pavlov <denys.pavlov@gmail.com>  
ENV PT_VERSION="1.2-rc-1"  
RUN apt-get update \  
&& apt-get -y install maven \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /mnt  
  
# jetty port  
EXPOSE 8080  
# debug port, if on.  
EXPOSE 5050  
CMD ["/mnt/start.sh"]  
ENTRYPOINT ["/entrypoint.sh"]  
  
ADD entrypoint.sh /entrypoint.sh  


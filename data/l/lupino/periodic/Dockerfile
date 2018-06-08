FROM busybox:ubuntu-14.04  
MAINTAINER Li Meng Jun "lmjubuntu@gmail.com"  
ADD ./periodic /usr/bin/periodic  
  
ENV PERIODIC_PORT tcp://:5000  
EXPOSE 5000  
ENTRYPOINT ["periodic"]  
  
CMD ["-d"]  


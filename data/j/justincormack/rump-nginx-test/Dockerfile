# Simple example with rump-nginx-lua  
FROM justincormack/rump-nginx  
  
MAINTAINER Justin Cormack  
  
COPY . /usr/src/rump-nginx-test  
  
WORKDIR /usr/src/rump-nginx-test  
  
ENV SUDO_UID=1000  
RUN ./build.sh  
  
ENV RUMP_VERBOSE=1  
EXPOSE 80  
CMD ["/usr/src/rump-nginx-test/nginx.sh"]  


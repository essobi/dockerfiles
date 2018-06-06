FROM trapexit/s6-ubuntu:1.19.1.1-16.04  
ADD files /tmp  
RUN /tmp/setup/install  
ENTRYPOINT ["/init"]  
EXPOSE 5900 6080  


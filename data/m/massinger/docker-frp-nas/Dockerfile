FROM resin/armv7hf-debian  
RUN [ "cross-build-start" ]  
COPY frps /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/frps && \  
mkdir /etc/frp  
  
COPY frps.ini /etc/frp/  
  
CMD ["frps", "-c", "/etc/frp/frps.ini"]  
  
RUN [ "cross-build-end" ]  


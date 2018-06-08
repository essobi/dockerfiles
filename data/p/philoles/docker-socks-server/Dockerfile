FROM centos:7.3.1611  
RUN mkdir -p /var/socks-server  
COPY data/* /var/socks-server/  
RUN chmod +x /var/socks-server/linux_amd64  
  
EXPOSE 40342  
EXPOSE 40342/udp  
  
CMD ["/var/socks-server/linux_amd64"]  


FROM centos:7.3.1611  
RUN mkdir -p /var/songj  
COPY data/* /var/songj/  
RUN chmod +x /var/songj/linux_amd64  
  
EXPOSE 55555  
CMD ["/var/songj/linux_amd64"]  


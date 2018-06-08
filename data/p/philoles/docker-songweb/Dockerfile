FROM centos:7.3.1611  
RUN mkdir -p /var/songweb  
COPY data/* /var/songweb/  
RUN mkdir /var/songweb/template  
RUN chmod -R 777 /var/songweb/*  
  
EXPOSE 44445  
CMD ["/var/songweb/sweb_linux_amd64"]  


FROM centos:7.3.1611  
RUN mkdir -p /var/songp  
COPY data/* /var/songp/  
RUN mkdir /var/songp/checktype /var/songp/config /var/songp/leechurl
/var/songp/template  
RUN chmod -R 777 /var/songp/*  
  
EXPOSE 44444  
CMD ["/var/songp/linux_amd64"]  


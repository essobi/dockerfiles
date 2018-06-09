FROM takashiabe/centos7-systemed-japanese  
  
RUN yum -y install httpd  
  
RUN yum clean all  
  
RUN usermod -u 1000 apache && groupmod -g 1000 apache  
  
RUN systemctl enable httpd.service  
  
EXPOSE 80  
CMD ["/usr/sbin/init"]  


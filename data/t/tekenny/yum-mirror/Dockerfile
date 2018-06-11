FROM centos:7  
COPY yum.repos.d/* /repo.def/  
COPY files/* /files/  
COPY nginx.conf /tmp/  
COPY env.sh prepare.sh refresh.sh /usr/local/bin/  
RUN /usr/local/bin/prepare.sh  
EXPOSE 80  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  


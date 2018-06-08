FROM centos:7  
# Install Nginx  
ADD nginx.repo /etc/yum.repos.d/  
RUN cd /tmp && \  
curl -O http://nginx.org/keys/nginx_signing.key && \  
rpm --import nginx_signing.key && \  
yum update -y && \  
yum install -y nginx  
  
# Clean Up  
RUN yum clean all && rm -rf /tmp/nginx*  
  
# Replace default nginx with 101-Nginx  
RUN rm -rf /etc/nginx  
ADD 101-nginx /etc/nginx  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]


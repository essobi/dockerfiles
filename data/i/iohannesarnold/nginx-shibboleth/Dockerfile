FROM centos:centos6  
  
# Add special nginx repo  
ADD jcu-eresearch.repo /etc/yum.repos.d/  
RUN yum -y update  
RUN yum -y install nginx  
  
ADD nginx /etc/nginx  
  
# Set up integration aspects  
EXPOSE 80  
EXPOSE 443  
CMD ["nginx"]  


FROM centos:7  
RUN yum -y install epel-release \  
&& yum -y install nginx  
  
ADD index.html /usr/share/nginx/html/index.html  
  
VOLUME /usr/share/nginx/html  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  


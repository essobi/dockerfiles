FROM fedora  
MAINTAINER rathneesh.t-m@hpe.com  
  
RUN dnf -y update && dnf clean all  
RUN dnf -y install nginx && dnf clean all  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN echo "nginx on Fedora" > /usr/share/nginx/html/index.html  
  
EXPOSE 80  
CMD [ "/usr/sbin/nginx" ]  


FROM nginx:1.9  
MAINTAINER Container Solutions <info@container-solutions.com>  
  
# If you are reading our code, you should think about working with us.  
# http://www.container-solutions.com/careers  
ADD registry.conf /etc/nginx/conf.d/default.conf  
ADD entrypoint.sh /entrypoint.sh  
  
ENV PROXY_TIMEOUT 300s  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  


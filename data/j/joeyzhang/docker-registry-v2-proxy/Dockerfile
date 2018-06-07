FROM nginx:1.7  
MAINTAINER Joeylulu  
  
# in order to test the function of automated build, I use the project from  
# https://github.com/ContainerSolutions/docker-registry-proxy  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  


# GaGa Test Dockerfile Test Version: 0.0.1  
FROM ubuntu:14.04  
MAINTAINER JiaJia "gagahappy@163.com"  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN echo 'Hi, I am in you container' > /usr/share/nginx/html/index.html  
EXPOSE 80  
# CMD ["/bin/ls", "-ls"]  
# ENTRYPOINT ["/usr/sbin/nginx"]  
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]  
  
# 如果启动容器时没有指定参数,则CMD的-h参数会被传给上面的ENTRYPOINT ["/usr/sbin/nginx"]  
# 如果启动容器指定了参数,则指定的参数会传给ENTRYPOINT  
# CMD ["-h"]


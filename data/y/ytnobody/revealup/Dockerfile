FROM ytnobody/base:wheezy  
MAINTAINER ytnobody@gmail.com  
  
ENV MANAGER_PORT 5555  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN cpanm -n App::revealup Proc::Simple Furl Plack::App::Proxy
HTML::FillInForm  
  
RUN mkdir /app  
ADD manager /app/manager  
ADD run /app/run  
ADD nginx_vhost.conf /etc/nginx/conf.d/nginx_vhost.conf  
RUN chmod +x /app/run  
  
EXPOSE 7777  
ENTRYPOINT ["/app/run"]  


FROM ubuntu:trusty  
  
RUN apt-get update  
RUN apt-get install -y munin nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN mkdir -p /etc/munin-access  
ADD nginx.conf /etc/nginx/sites-enabled/default  
  
CMD /etc/init.d/munin start; nginx  


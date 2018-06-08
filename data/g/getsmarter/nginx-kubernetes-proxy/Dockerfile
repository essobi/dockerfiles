FROM nginx:1.11.8  
# Forward nginx access and error logs to stdout and stderr  
RUN ln -sf /proc/1/fd/1 /var/log/nginx/access.log \  
&& ln -sf /proc/1/fd/2 /var/log/nginx/error.log  
  
# Install nano and dnsutils  
RUN apt-get update && apt-get install -y nano dnsutils  
  
# Set terminal  
RUN echo 'export TERM=xterm' >> /root/.bashrc  
  
COPY conf/nginx.conf /etc/nginx/nginx.conf  
  
COPY conf/proxy.conf /etc/nginx/conf.d/default.conf  
  
COPY html/ /usr/share/nginx/html/  
  
CMD ["nginx", "-g", "daemon off;"]  


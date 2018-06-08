FROM nginx:1.13  
# Install openssh-server to provide web ssh access from kudu, supervisor to
run processor  
RUN apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
supervisor \  
openssh-server \  
&& echo "root:Docker!" | chpasswd  
  
# forward request and error logs to docker log collector  
RUN mkdir -p /home/LogFiles \  
&& ln -sf /dev/stdout /home/LogFiles/access.log \  
&& ln -sf /dev/stderr /home/LogFiles/error.log  
  
COPY config/nginx.conf /etc/nginx/nginx.conf  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY config/sshd_config /etc/ssh/  
COPY app/hostingstart.html /home/site/wwwroot/hostingstart.html  
COPY scripts/start.sh /bin/  
  
EXPOSE 80 2222  
CMD ["/bin/start.sh"]


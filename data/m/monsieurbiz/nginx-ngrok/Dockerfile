FROM nginx  
  
LABEL maintainer="Monsieur Biz <docker@monsieurbiz.com>"  
  
COPY files/bin/ngrok /usr/bin/ngrok  
COPY files/vhost.conf /etc/nginx/conf.d/default.conf  
COPY files/run.sh /run.sh  
  
RUN chmod +x /usr/bin/ngrok /run.sh  
  
VOLUME /root/.ngrok2  
VOLUME /local  
  
EXPOSE 4040  
CMD ["/run.sh"]  
  


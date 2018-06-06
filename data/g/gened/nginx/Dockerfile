FROM nginx:1.10.1  
RUN rm -rf /etc/nginx  
COPY etc/nginx/ /etc/nginx/  
COPY run.sh /  
VOLUME /etc/nginx  
  
CMD ["/run.sh"]  


FROM nginx  
  
ADD entrypoint.sh /root/entrypoint.sh  
RUN chmod +x /root/entrypoint.sh \  
&& rm /etc/nginx/conf.d/default.conf  
ADD registry-proxy.conf /etc/nginx/conf.d/  
CMD /root/entrypoint.sh  


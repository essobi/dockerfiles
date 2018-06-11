FROM gliderlabs/alpine:3.2  
RUN apk-install nginx  
  
RUN rm -r /var/lib/nginx  
RUN ln -s /data/.nginx/lib /var/lib/nginx  
RUN rmdir /var/log/nginx  
RUN ln -s /data/.nginx/log /var/log/nginx  
CMD ["/host/nginx/run"]  


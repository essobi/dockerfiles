FROM alpine:3.5  
RUN apk add --no-cache \  
nginx \  
bash  
  
ENV VISUAL=vi  
RUN mkdir -p /var/log/nginx  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log  
  
RUN mkdir /data && mkdir /app  
VOLUME ["/data"]  
  
WORKDIR /app  
COPY nginx.conf /etc/nginx/  
COPY app/ /app/  
  
EXPOSE 80  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["server"]  


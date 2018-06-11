FROM alpine:3.5  
EXPOSE 80  
RUN \  
apk add --update nginx && \  
rm /etc/nginx/nginx.conf && \  
ln -s /app/nginx.conf /etc/nginx/nginx.conf && \  
mkdir /run/nginx  
  
ADD . /app  
  
CMD ["ash", "-cex", "/app/start.sh"]  
  


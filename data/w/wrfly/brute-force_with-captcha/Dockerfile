# Micro docker  
FROM alpine:latest  
MAINTAINER wrfly mr.wrfly@gmail.com  
  
# Install php  
RUN apk --update add php5-fpm php5-gd  
  
# Expose port  
EXPOSE 80  
# Copy a phpcaptcha  
COPY phpcaptcha /app  
  
# Copy init script  
COPY fc-init.sh top_1000.txt /  
  
RUN chmod +x fc-init.sh  
  
# Start  
CMD ["/fc-init.sh"]  


# Dockerfile for a simple Nginx stream replicator  
FROM alpine:3.4  
# Set up user  
ENV USER nginx  
RUN adduser -s /sbin/nologin -D -H ${USER}  
  
# Install prerequisites and update certificates  
RUN apk --update --no-cache add \  
nginx-rtmp \  
ffmpeg && \  
rm -rf /var/cache/apk/*  
  
# Create nginx rtmp tmp hls and dash directories  
RUN mkdir -p /tmp/hls && \  
mkdir -p /tmp/dash  
  
# Create nginx html directories  
RUN mkdir -p /usr/share/nginx/html  
RUN mkdir -p /etc/nginx/sites-available  
RUN mkdir -p /etc/nginx/conf.d  
  
RUN rm -f /etc/nginx/nginx.conf  
  
VOLUME [ "/usr/share/nginx/html", "/etc/nginx" ]  
  
# Set up the html directory  
#COPY /assets/usr/share/nginx/html/ /usr/share/nginx/html/  
# Set up config file  
#COPY /assets/etc/nginx /etc/nginx/  
# Forward logs to Docker  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Run the application  
USER ${USER}  
  
EXPOSE 1935 8080 8443  
CMD ["nginx", "-g", "pid /tmp/nginx.pid; daemon off;"]


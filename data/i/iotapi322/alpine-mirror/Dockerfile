#  
# Run lighttpd to serve apk packages  
#  
FROM alpine:3.4  
RUN apk --no-cache add bash lighttpd rsync  
ADD lighttpd.conf /etc/lighttpd/lighttpd.conf  
  
# add the script that will sync with the alpine home base  
ADD rsync.sh /etc/periodic/hourly/package-rsync  
RUN chmod +x /etc/periodic/hourly/package-rsync  
ADD exclude.txt /etc/rsync/exclude.txt  
# actual command to run crond is in startup.sh  
#  
# Add the simple startup script  
ADD startup.sh /usr/local/bin/startup.sh  
RUN chmod +x /usr/local/bin/startup.sh  
  
RUN mkdir -p /var/www/localhost/htdocs/alpine  
RUN chmod +x /etc/periodic/hourly/package-rsync  
  
VOLUME /var/www/localhost/htdocs/alpine  
  
CMD ["startup.sh"]  
EXPOSE 80  


FROM node:8  
# Copy contents of sample folder to /var/www/sample and run npm install to get
all dependencies  
COPY sample/ /var/www/sample  
RUN cd /var/www/sample  
#\  
#&& npm install  
# Copy the entrypoint file, set permissions and create volume  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh \  
&& usermod -u 1001 node \  
&& groupmod -g 1001 node  
VOLUME /var/www/app  
  
# Run entrypoint bash script that  
ENTRYPOINT ["/entrypoint.sh"]  
WORKDIR /var/www/app  
  
# Expose port for container and run npm start sequence  
EXPOSE 8080  
CMD npm install && npm start


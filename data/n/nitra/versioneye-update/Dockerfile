FROM node:0.10  
ENV API_KEY ""  
ENV PROJECT_ID ""  
ENV PROJECT_FILE ""  
RUN mkdir -p /var/www  
RUN npm install -g versioneye-update  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["start.sh"]


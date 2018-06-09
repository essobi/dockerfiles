FROM node:6  
CMD ["/usr/local/bin/parse-dashboard"]  
EXPOSE 4040  
RUN npm install -g parse-dashboard  
  
ENV MOUNT_PATH /  
ENV PARSE_DASHBOARD_ALLOW_INSECURE_HTTP yes  
ENV PARSE_DASHBOARD_APP_NAME "Parse App"  


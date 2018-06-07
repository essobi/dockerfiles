FROM node:4.4.3  
# Bundle app source  
COPY . /src  
RUN rm -rf /src/node_modules  
RUN rm -rf /src/varnish  
RUN rm -rf /src/supervisord  
RUN rm -rf /src/startup.sh  
  
# Install app dependencies  
RUN cd /src; npm install  
  
# Copy startup script  
ADD startup.sh /apps/  
RUN chmod +x /apps/startup.sh  
  
EXPOSE 8000 6081 9001  
CMD ["/bin/sh", "-c" , "node /src/app.js"]


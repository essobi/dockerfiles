FROM node:6.9.2  
ENV node_env production  
COPY . /opt/rds-rdmp-portal/  
RUN chmod +x /opt/rds-rdmp-portal/buildTypescript.sh  
RUN cd /opt/rds-rdmp-portal && ./buildTypescript.sh  
RUN echo "Australia/Brisbane" > /etc/timezone && dpkg-reconfigure -f
noninteractive tzdata  
CMD NODE_ENV=$node_env node app.js  


FROM node:slim  
  
RUN mkdir /app  
RUN mkdir /app/data  
WORKDIR /app  
  
RUN apt-get update  
RUN apt-get -y install cron git  
  
COPY package.json /app  
RUN npm install --only=prod  
  
COPY dist /app  
  
COPY run.sh /app  
RUN chmod +x /app/run.sh  
  
COPY crontab /tmp/crontab  
RUN touch /etc/cron.d/ipci-cron  
RUN chmod 0644 /etc/cron.d/ipci-cron  
RUN touch /var/log/cron.log  
  
CMD ["/app/run.sh"]  


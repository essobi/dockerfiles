FROM node:7  
RUN touch /etc/apt/sources.list.d/postgresql.list && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main 9.5" >>
/etc/apt/sources.list.d/postgresql.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.4.list && \  
apt-get update && \  
apt-get install -y mongodb-org-tools postgresql-client-9.5 cron nano  
ADD crontab /root/  
RUN crontab /root/crontab  
RUN touch /var/log/cron.log  
WORKDIR /schulcloud-backup  
COPY . .  
RUN npm install  
  
CMD cron && npm start  


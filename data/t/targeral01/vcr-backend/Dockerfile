FROM ubuntu:xenial  
  
RUN apt-get update -y && \  
apt-get install wget git -y && \  
wget -P /tmp/ https://deb.nodesource.com/setup_9.x && \  
bash /tmp/setup_9.x && \  
apt-get install nodejs -y && \  
rm -rf /var/lib/apt/lists/* && \  
npm cache clean --force && \  
mkdir /code/  
ADD . /code/  
RUN cd /code/ && npm install pm2 -g && npm install  
EXPOSE 3030  
WORKDIR /code/  
CMD ["npm", "run", "pm2"]  
#CMD ["pm2-runtime", "app.js"]  


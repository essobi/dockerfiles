FROM node:6.11.0-slim  
MAINTAINER Joyson Dsouza  
  
LABEL version="1.3.0"  
LABEL description="Docker file for Lemoney Broker Server"  
  
RUN ln -sf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime  
  
# Install PM2  
RUN npm install -g pm2  
  
RUN mkdir -p /usr/src/  
WORKDIR /usr/src/  
COPY . /usr/src/  
  
RUN npm install .  
  
EXPOSE 8888  
ENV DB_TYPE=postgres  
ENV DB_HOST=144.1.1.242  
ENV DB_NAME=lemoney  
ENV DB_USER=lemoney  
ENV DB_PWD=lemoney  
  
ENV NODE_ENV=development  
ENV TRACE_PATH=/usr/src/traces/  
ENV TRACE_HIST_PATH=/usr/src/tracesHistory/  
ENV TRACE_BACKUP_PATH=/usr/src/tracesBackup/  
ENV TRACE_MAX_FILE_SIZE=1048576  
CMD pm2 start --no-daemon processes.json  


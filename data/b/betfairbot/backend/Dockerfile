FROM node:8  
RUN apt update -y && \  
apt upgrade -y && \  
apt install -y cron rsyslog  
  
ADD cronfile /etc/cron.d/betfairbot  
RUN crontab /etc/cron.d/betfairbot  
RUN chmod 0644 /etc/cron.d/betfairbot  
  
# Add these lines to your own Dockerfile  
RUN touch /var/log/cron.log  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN yarn install && \  
yarn build  
  
CMD printenv >> /etc/environment && touch /etc/cron.d/betfairbot && rsyslogd
&& cron && tail -F /var/log/syslog /var/log/cron.log  


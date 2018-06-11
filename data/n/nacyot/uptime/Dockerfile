FROM dockerfile/ubuntu  
MAINTAINER Daekwon Kim <propellerheaven@gmail.com>  
  
RUN \  
cd /opt &&\  
wget -O /opt/nodejs.tar.gz
http://nodejs.org/dist/v0.10.33/node-v0.10.33-linux-x64.tar.gz &&\  
tar xvf nodejs.tar.gz &&\  
mv /opt/node-v0.10.33-linux-x64 /opt/nodejs &&\  
bash -c "ln -s /opt/nodejs/bin/{node,npm} /usr/local/bin/"  
  
RUN \  
apt-get update &&\  
apt-get install -y mongodb git python  
  
WORKDIR /opt/uptime  
RUN \  
git clone https://github.com/nacyot/uptime.git /opt/uptime &&\  
cd /opt/uptime &&\  
npm install  
  
RUN \  
npm install lodash moment https://github.com/nacyot/uptime-
slack/archive/0.0.4.tar.gz --save &&\  
npm install  
  
ENV MONGODB_HOST_PORT 172.17.42.1:27017  
ENV MONGODB_DATABASE uptime  
ENV MONGODB_USER root  
# ENV MONGODB_PASSWORD  
ENV EMAIL_SERVICE Gmail  
# ENV EMAIL_USER  
# ENV EMAIL_PASSWORD  
# ENV EMAIL_FROM  
# ENV EMAIL_TO  
# ENV SLACK_NOTIFY  
# ENV SLACK_HOOK  
# ENV UPTIME_URL  
# ENV SLACK_CHANNEL  
# ENV SLACK_NAME  
ADD ./files/ /root/files  
RUN \  
chmod +x /root/files/*.sh &&\  
mv /root/files/default.yaml /opt/uptime/config/default.yaml &&\  
mv /root/files/slack.yaml /opt/uptime/config/slack.yaml &&\  
mv /root/files/index.js /opt/uptime/plugins/index.js  
  
EXPOSE 8082  
CMD /root/files/setup_configs.sh && /root/files/run.sh  
  


FROM resin/nuc-node  
  
RUN mkdir -p /usr/src/app && ln -s /usr/src/app /app  
ONBUILD COPY zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf  
ONBUILD COPY . /usr/src/app  
ONBUILD WORKDIR /usr/src/app  
ONBUILD RUN DEBIAN_FRONTEND=noninteractive JOBS=MAX npm install --unsafe-perm  
ONBUILD RUN node_modules/.bin/bower --allow-root --config.interactive=false
install  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y xorg chromium xinput
cron lm-sensors libodbc1  
RUN wget http://repo.zabbix.com/zabbix/3.0/debian/pool/main/z/zabbix/zabbix-
agent_3.0.3-1+jessie_amd64.deb  
RUN dpkg -i zabbix-agent_3.0.3-1+jessie_amd64.deb  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y zabbix-agent  
  
CMD [ "npm", "start" ]  


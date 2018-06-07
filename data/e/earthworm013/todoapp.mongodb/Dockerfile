FROM alpine:3.7 as SystemOS  
RUN mkdir -p /data/db /data/configdb \  
&& apk add --no-cache mongodb  
EXPOSE 27017  
  
FROM SystemOS  
COPY './mongo_initial_script.js' /data/mongo_initial_script.js  
RUN mongod --bind_ip 0.0.0.0 & \  
sleep 10 \  
&& mongo --eval "load('/data/mongo_initial_script.js');" \  
&& mongod --shutdown  
  
CMD ["mongod", "--auth", "--bind_ip", "0.0.0.0"]  
  
# FROM debian:jessie-slim  
# COPY './mongo_initial_script.js' /data/mongo_initial_script.js  
  
# RUN mkdir -p /data/db /data/configdb \  
# && apt-get update \  
# && apt-get install -y sudo \  
# && sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 \  
# && echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.6 main"
| sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list \  
# && sudo apt-get update \  
# && sudo apt-get install -y mongodb-org=3.6.3 mongodb-org-server=3.6.3
mongodb-org-shell=3.6.3 mongodb-org-mongos=3.6.3 mongodb-org-tools=3.6.3 \  
# && echo "mongodb-org hold" | sudo dpkg --set-selections \  
# && echo "mongodb-org-server hold" | sudo dpkg --set-selections \  
# && echo "mongodb-org-shell hold" | sudo dpkg --set-selections \  
# && echo "mongodb-org-mongos hold" | sudo dpkg --set-selections \  
# && echo "mongodb-org-tools hold" | sudo dpkg --set-selections \  
# && apt-get clean \  
# && apt-get autoremove \  
# && sudo apt-get clean \  
# && sudo apt-get autoremove  
  
# RUN mongod --bind_ip_all --quiet & \  
# sleep 10 \  
# && mongo --eval "load('/data/mongo_initial_script.js');" \  
# && mongod --shutdown  
# EXPOSE 27017  
# CMD ["mongod", "--auth", "--bind_ip_all"]


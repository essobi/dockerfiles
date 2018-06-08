# Docker file with NODE-RED https support  
#  
FROM centos  
  
MAINTAINER geocentricllc  
  
ADD run-node-red.sh /usr/local/bin/run-node-red.sh  
  
ADD settings.js /tmp/settings-tmpl.js  
  
RUN yum -y install epel-release && yum -y install openssl && yum -y install
nodejs && yum -y install npm && npm install -g node-red && chmod +x
/usr/local/bin/run-node-red.sh  
  
RUN npm install -g node-red-contrib-pubnub && npm install -g node-red-contrib-
nest && npm install -g node-red-node-aws && npm install -g node-red-node-box
&& npm install -g node-red-node-delicious && npm install -g node-red-node-
dropbox && npm install -g node-red-node-fitbit && npm && npm install -g node-
red-node-google && npm install -g node-red-node-instagram && npm install -g
node-red-node-jawboneup && npm install -g node-red-node-openweathermap && npm
install -g node-red-node-pinboard && npm install -g node-red-node-strava &&
npm install -g node-red-node-tfl && npm install -g node-red-node-weather-
underground  
  
EXPOSE 1880  
  
CMD /usr/local/bin/run-node-red.sh  


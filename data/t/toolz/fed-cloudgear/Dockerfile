FROM fedora:23  
MAINTAINER cloudgear10 <poke@cloudgear.io>  
RUN dnf -y update && dnf clean all  
RUN dnf install python make git wget -y  
#RUN dnf install wget unzip vim -y  
RUN dnf install -y nodejs npm  
RUN npm install -g grunt-cli  
#RUN dnf install gcc ruby-devel rubygems -y  
#RUN gem install dashing  
#RUN gem install bundler  
#RUN cd /opt && dashing new cloudgear  
#RUN cd /opt/cloudgear && bundle  
RUN cd /opt && git clone https://github.com/node-red/node-red.git  
RUN cd /opt/node-red && npm install  
RUN cd /opt/node-red && grunt build  
EXPOSE 1880  
EXPOSE 1881  
RUN cd /opt/node-red && npm install node-red-contrib-freeboard  
RUN cd /opt/node-red/node_modules/node-red-contrib-
freeboard/node_modules/freeboard/plugins/ && git clone
https://github.com/Freeboard/plugins.git  
RUN cd /opt/node-red/node_modules/node-red-contrib-
freeboard/node_modules/freeboard/plugins/plugins && mv * ../  
RUN cd /opt/node-red/node_modules/node-red-contrib-
freeboard/node_modules/freeboard/plugins/ && rm -rf plugins  
RUN cd /opt/node-red/node_modules/node-red-contrib-
freeboard/node_modules/freeboard/ && sed -i.bak -e '13d' index.html  
RUN cd /opt/node-red/node_modules/node-red-contrib-
freeboard/node_modules/freeboard/ && sed -i
'13ihead.js("js/freeboard.js","js/freeboard.plugins.min.js",
"../freeboard_api/datasources","plugins/datasources/plugin_json_ws.js","plugins/datasources/plugin_node.js",'
index.html  
RUN cd /opt/node-red && npm install node-red-node-mongodb  
RUN cd /opt/node-red && npm install node-red-contrib-mongodb2  
#RUN cd /opt/node-red && npm install node-red-contrib-salesforce  
RUN cd /opt/node-red && npm install node-red-contrib-couchdb  
RUN cd /opt/node-red && npm install node-red-contrib-influxdb  
RUN cd /opt/node-red && npm install npm install node-red-contrib-googlechart  
#RUN cd /opt/cloudgear/  
CMD ["node", "/opt/node-red/red.js"]  


FROM nodered/node-red-docker:v8  
  
USER root  
  
WORKDIR /usr/src/node-red  
  
RUN apt-get update  
  
# ---- USB ----  
# Add nodes  
RUN npm i -S node-red-node-serialport  
  
# ---- ZWAVE ----  
# Install latest OpenZwave library  
RUN apt-get -y install libudev-dev  
RUN mkdir -pv /usr/src/  
RUN git clone https://github.com/OpenZWave/open-zwave.git /usr/src/open-zwave  
RUN cd /usr/src/open-zwave && make && make install  
ENV LD_LIBRARY_PATH /usr/local/lib64  
RUN ldconfig /usr/local/lib64  
  
# Add openzwave nodes  
RUN npm i -S node-red-contrib-openzwave  
  
# ---- ADD JS LIBRARIES ----  
RUN npm i -S moment  
RUN npm i -S moment-ferie-fr  
  
# ---- ADD CUSTOM NODES ----  
RUN npm i -S git+https://github.com/Neonox31/node-red-web-nodes.git  
RUN npm i -S node-red-node-pushover  
RUN npm i -S node-red-contrib-broadlink  
RUN npm i -S node-red-contrib-scheduler  
RUN npm i -S node-red-contrib-advanced-ping  
RUN npm i -S node-red-contrib-repeat  
RUN npm i -S node-red-contrib-ghome  
RUN npm i -S node-red-node-google  
RUN npm i -S node-red-node-forecastio  
  
# --------------------------------  
# User configuration directory volume  
EXPOSE 1880  
# Environment variable holding file path for flows configuration  
ENV FLOWS=flows.json  
  
CMD npm start -- --userDir /data  


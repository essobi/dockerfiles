FROM nodered/node-red-docker:latest  
  
USER root  
  
WORKDIR /usr/src/node-red  
  
# ---- ZWAVE ----  
# Install latest OpenZwave library  
RUN apt-get update  
RUN apt-get -y install libudev-dev  
RUN mkdir -pv /usr/src/  
RUN git clone https://github.com/OpenZWave/open-zwave.git /usr/src/open-zwave  
RUN cd /usr/src/open-zwave && make && make install  
ENV LD_LIBRARY_PATH /usr/local/lib64  
RUN ldconfig /usr/local/lib64  
  
# Add openzwave nodes  
RUN npm i -S node-red-contrib-openzwave  
  
# ---- ADD CUSTOM NODES ----  
# --------------------------------  
# User configuration directory volume  
EXPOSE 1880  
# Environment variable holding file path for flows configuration  
ENV FLOWS=flows.json  
  
CMD ["npm", "start", "--", "--userDir", "/data"]  


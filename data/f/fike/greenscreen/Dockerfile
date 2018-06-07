FROM node:8.9.4  
ENV GREENSCREEN_HOME /opt/greenscreen  
  
RUN git clone https://github.com/groupon/greenscreen.git ${GREENSCREEN_HOME}
&& \  
adduser --gecos " " \--disabled-password greenscreen && \  
cd /opt/greenscreen && \  
npm install && \  
rm -rf ${GREENSCREEN_HOME}/.git  
  
ADD start ${GREENSCREEN_HOME}/start  
  
WORKDIR ${GREENSCREEN_HOME}  
  
EXPOSE 4994  
ENTRYPOINT ${GREENSCREEN_HOME}/start  


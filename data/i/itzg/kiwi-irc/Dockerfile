FROM node:7  
RUN cd /opt && git clone https://github.com/prawnsalad/KiwiIRC.git  
  
WORKDIR /opt/KiwiIRC  
  
EXPOSE 7778  
RUN npm install  
  
COPY config.js /opt/KiwiIRC  
  
RUN ./kiwi build  
  
ENTRYPOINT ["/opt/KiwiIRC/kiwi","-f","start"]  


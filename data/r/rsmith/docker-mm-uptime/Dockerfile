FROM node:0.10  
RUN git clone git://github.com/fzaninotto/uptime.git /tmp/uptime  
RUN cd /tmp/uptime && npm install  
  
ENV NODE_ENV=production  
  
COPY get_certs.js /tmp/  
COPY package.json /tmp/  
COPY production.yaml /tmp/uptime/config/  
COPY run.sh /usr/bin/run.sh  
  
EXPOSE 80  
CMD /usr/bin/run.sh


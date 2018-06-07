FROM kkarczmarczyk/node-yarn:6.9-slim  
  
RUN mkdir -p /opt/app/ \  
&& mkdir -p /opt/app/files/scenarios/ \  
&& mkdir -p /opt/app/files/reports/  
  
VOLUME /opt/app/files  
  
WORKDIR /opt/app  
  
# Copy app code  
COPY package.json yarn.lock ./  
COPY node_modules node_modules  
COPY assets assets  
COPY server server  
COPY build build  
  
EXPOSE 3001  
CMD cd /opt/app \  
&& npm run start:prod  


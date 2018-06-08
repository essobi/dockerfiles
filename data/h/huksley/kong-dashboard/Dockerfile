FROM alpine  
RUN mkdir -p /data/kong-dashboard && \  
apk update && apk add curl git nodejs && \  
npm install -g bower  
  
COPY .bowerrc /data  
COPY bower.json /data  
COPY material-icons.patch /data  
  
RUN cd /data && \  
git clone https://github.com/PGBI/kong-dashboard/ /data/kong-dashboard && \  
ls -la && \  
patch -p0 <material-icons.patch && \  
cd /data/kong-dashboard && \  
npm install && \  
npm run install && \  
cd /data && \  
bower update --allow-root && \  
true  
  
WORKDIR /data/kong-dashboard  
EXPOSE 8080  
CMD npm run start  
  


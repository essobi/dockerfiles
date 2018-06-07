FROM node:5  
RUN npm install -g pm2  
WORKDIR /usr/src/app  
RUN git clone https://github.com/prerender/prerender.git .  
RUN npm install  
ENV PORT=5000  
ENV PRERENDER_SERVICE_URL=http://localhost:5000  
ENV PRERENDER_NUM_WORKERS=1  
CMD ["pm2", "start", "server.js", "-i", "1", "--no-daemon"]  


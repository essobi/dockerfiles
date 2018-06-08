FROM node  
  
WORKDIR /home/dist  
ADD / /home/dist  
  
RUN npm install -g bower && \  
bower install --force-latest --config.interactive=false \--allow-root
bower.json && \  
npm install -g gulp && \  
npm install  
  
EXPOSE 9000


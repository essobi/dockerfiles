FROM sesteva/yeoman  
  
RUN npm install -g generator-polymer  
  
RUN mkdir -p /home/project && \  
chmod 777 -R /home/project  
  
CMD cd /home/project && \  
npm install && \  
bower install --allow-root && \  
grunt serve  
  
WORKDIR /home/project  
  
EXPOSE 9000  


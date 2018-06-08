FROM node  
  
RUN useradd -rm -G www-data docker  
  
EXPOSE 9871  
VOLUME ./application /home/docker  
  
USER docker  
  
WORKDIR /home/docker  
  
CMD /bin/bash -c "npm install && node index.js"  


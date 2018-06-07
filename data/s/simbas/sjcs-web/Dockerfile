FROM node:8  
RUN npm i -g reveal-md@1.1.3 http-server@0.11.1  
  
WORKDIR /usr/local/web/  
  
COPY kali-setup.sh /usr/local/web/scripts/kali-setup.sh  
COPY entrypoint.sh /usr/local/web/entrypoint.sh  
  
ENTRYPOINT ["./entrypoint.sh"]  


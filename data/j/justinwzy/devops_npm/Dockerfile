FROM node:7.8.0-alpine  
  
COPY sleep.sh .  
  
RUN chmod 777 sleep.sh  
  
VOLUME /root/  
  
VOLUME /usr/local/lib/node_modules/  
  
CMD ["./sleep.sh"]  


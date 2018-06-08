FROM ghost:alpine  
  
ENV NODE_ENV production  
  
COPY custom-entrypoint.sh /usr/local/bin/  
COPY config-template.js /  
  
ENTRYPOINT ["custom-entrypoint.sh"]  
CMD ["npm", "start"]


FROM emmanuelgautier/node:8.9-centos  
  
LABEL MAINTAINER Emmanuel Gautier <docker@emmanuelgautier.fr>  
  
# Install pm2  
RUN npm install pm2 -g  
  
EXPOSE 80 443 43554  
# Start pm2.json process file  
CMD ["pm2-runtime", "start", "pm2.json"]  

